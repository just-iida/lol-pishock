import requests
import json
import time
import urllib3
import os.path
import shutil

# disable https warning -- future me, replace with an implementation of the root certificate for security purposes
urllib3.disable_warnings()

# colors used for printing, "stolen" from blender
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# check if config file exists, if yes, read it, if not then create new using configtemplate
print(f'{bcolors.BOLD}{bcolors.OKCYAN}Checking for config file...{bcolors.ENDC}\n')
time.sleep(1)
if os.path.exists('config.config'):
    with open('config.config') as config:
        shock = json.load(config)
        print(f'{bcolors.BOLD}{bcolors.UNDERLINE}{bcolors.OKGREEN}Config loaded successfully.{bcolors.ENDC}\n')
        time.sleep(2)
else:
    print(f'{bcolors.BOLD}{bcolors.WARNING}\n --- \n{bcolors.UNDERLINE}Config file was not found, attempting to create a new one based on configtemplate.\n --- \n{bcolors.ENDC}')
    try:
        shutil.copyfile('configtemplate', 'config.config')
        print(f'{bcolors.BOLD}{bcolors.OKBLUE}\n --- \n{bcolors.UNDERLINE}New config file has been created!{bcolors.ENDC}{bcolors.BOLD}{bcolors.OKBLUE}\n --- \n{bcolors.UNDERLINE}Fill in your Username, Apikey and Code, then restart LoL-PiShock{bcolors.ENDC}{bcolors.BOLD}{bcolors.OKBLUE}\n --- \n{bcolors.ENDC}')
        exit()
    except PermissionError:
        print(f"{bcolors.BOLD}{bcolors.FAIL}\n ---\n{bcolors.UNDERLINE}Error occurred while creating config file.{bcolors.ENDC}\n {bcolors.BOLD}{bcolors.FAIL}---{bcolors.ENDC}")
        exit()


# check if config still has default values
username = shock["Username"]
apikey = shock["Apikey"]
code = shock["Code"]
if username == "PISHOCK-USERNAME":
    print(f'{bcolors.BOLD}{bcolors.FAIL}Your config file still contains the default value for USERNAME, change it and restart LoL-PiShock.{bcolors.ENDC}')
    exit()
if apikey == "PISHOCK-APIKEY":
    print(f'{bcolors.BOLD}{bcolors.FAIL}Your config file still contains the default value for APIKEY, change it and restart LoL-PiShock.{bcolors.ENDC}')
    exit()
if code == "PISHOCK-CODE":
    print(f'{bcolors.BOLD}{bcolors.FAIL}Your config file still contains the default value for CODE, change it and restart LoL-PiShock.{bcolors.ENDC}')
    exit()
# inform user of the values

op = shock["Op"]
if op == "0":
    operation = "Shock"
elif op == "1":
    operation = "Vibrate"
elif op == "2":
    operation = "Beep"
else:
    operation = f"{bcolors.FAIL}INVALID VALUE, the value for operation should be 0, 1 or 2{bcolors.ENDC}"
duration = shock["Duration"]
intensity = shock["Intensity"]
print(f'{bcolors.BOLD}{bcolors.HEADER}Current values for shocking:{bcolors.ENDC}', f'\n{bcolors.OKCYAN}Operation:{bcolors.ENDC}', operation, f'\n{bcolors.OKCYAN}Duration:{bcolors.ENDC}', duration, f'{bcolors.OKCYAN}\nIntensity:{bcolors.ENDC}', intensity + f'{bcolors.ENDC}')

running = True
while running:

    # define globals
    game = 0
    cooldown = 0

    # function to check if the game is running
    def check_process_running():
        global game
        try:
            API_playername = requests.get('https://127.0.0.1:2999/liveclientdata/activeplayername', verify=False)
            playername = API_playername.text
            summonername = json.loads(playername) [::-1]
            global victim
            victim = summonername.split("#")[1] [::-1]
            if game == 0:
                print(f"{bcolors.BOLD}{bcolors.OKBLUE}Game found, current player is:", victim + f'{bcolors.ENDC}')
                game = 1
        except:
            game = 0
            print(f"{bcolors.UNDERLINE}{bcolors.WARNING}Cannot detect a game running, retrying in 5 seconds.{bcolors.ENDC}")

    # while game not running, run a check for it every 5 seconds
    while not bool(game):
        print(f"\n{bcolors.OKGREEN}Checking for game...{bcolors.ENDC}\n")
        check_process_running()
        time.sleep(5)

    # while game is running, check for deaths and shock on death according to the config
    while bool(game):
        check_process_running()
        try:
            API_gamedata = requests.get('https://127.0.0.1:2999/liveclientdata/playerlist', verify=False)
            gamedata = API_gamedata.text
            plrnumber = [
                plr for plr in json.loads(gamedata)
                if plr['summonerName'] == victim
            ]
            player = json.dumps(plrnumber)
            dead = json.loads(player)[0]
            if dead["isDead"] == True:
                if cooldown == 0:
                    #do the shock here
                    print(f'{bcolors.BOLD}{bcolors.WARNING}Shock time!{bcolors.ENDC}')
                    requests.post('https://do.pishock.com/api/apioperate/', json = shock)
                    cooldown = 1
            else:
                if cooldown == 1:
                    cooldown = 0
        except requests.exceptions.ConnectionError:
            check_process_running()
        time.sleep(0.1) 