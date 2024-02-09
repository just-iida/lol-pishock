from riotwatcher import LolWatcher, ApiError
import pandas as pd
import configparser

#config
config =  configparser.ConfigParser()
config.readfp(open(r'config.config'))
lol_api_key = config.get('lol', 'api-key')
#watcher

watcher = LolWatcher(lol_api_key)

