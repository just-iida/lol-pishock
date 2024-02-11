# ⚡ LoL-PiShock
LoL-PiShock currently serves one function: shocking you when you die in League of Legends.
<br> Yes I missed the opportunity to call it LoL-PyShock, and yes I'll instead write about it here instead of renaming, no I'm not renaming it.
### ‼️ Disclaimer
LoL-PiShock is not responsible for any harm caused by misuse of the shock collar sold along with the PiShock device. We do not recommend putting any kind of electrical device near the heart or use if you have a heart condition. Shock collars are not meant for use on humans and can cause serious injury including cardiac events.
### ☕ Buy me coffee
https://ko-fi.com/mooniebuns
Giving money is completely optional and has the only purpose of motivating me to keep creating more.
## Installation and setup
**LoL-PiShock was developed using Python 3.12, there is no official support for other versions.**
### Requirements
* [Python 3.12](https://www.python.org/)
* ❓ Windows? Might work on Linux as long as the Live Client Data API works however is not officially supported.
### Installation
* ``git clone https://github.com/just-iida/lol-pishock.git``
* ``pip install -r requirements.txt``
### Setup
* Run ``py .\lol_pishock.py`` to create a ``config.config`` based on the ``configtemplate`` or alternatively create a file named ``config.config`` manually and copy the contents of ``configtemplate`` into it.
* Replace PISHOCK-USERNAME with your PiShock username.
* Replace PISHOCK-APIKEY with the Api Key generated at https://pishock.com/#/account
* Replace PISHOCK-CODE with the Code you get from https://pishock.com/#/control, clicking share and clicking **+ CODE**

You can edit the values of **Op**, **Duration** and **Intensity** as you please, keeping your safety in mind.
#### Op has 3 modes:
* 0 for shocking
* 1 for vibrating
* 2 for beeping
You may want to test functionality using the vibration or beep modes to make sure it works.
#### Duration must be between 1 and 15 (seconds)
#### Intensity must be between 1 and 100
## Future Plans
* ❓ Use [Python-PiShock](https://python-pishock.readthedocs.io/) API instead of PiShock API (Need to test first, might make another branch for it.)
* Editing config, for both shocking values and API functionality without restarting
* Graphical User Interface (no more console)
* ❓ Support for more than just shocking you on death.

# Legal
LoL-PiShock was created under Riot Games' "Legal Jibber Jabber" policy using assets owned by Riot Games.  Riot Games does not endorse or sponsor this project.
LoL-PiShock was created using the PiShock API. PiShock does not endorse or sponsor this project.
