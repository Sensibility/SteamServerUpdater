[![Build Status](https://superphage.us:8443/app/rest/builds/buildType\(id:SteamServerUpdater\)/statusIcon)](https://superphage.us:8443/viewType.html?buildTypeId=SteamServerUpdater&guest=1)

# SteamServerUpdater
Auto Updater for Steam Game Servers

## Dependencies
Requires:
* [Python 3](https://www.python.org/download/releases/3.0/)
* [Steamcmd](https://developer.valvesoftware.com/wiki/SteamCMD)

## Setup
After installing Python 3, goto the repo directory and run:
`python -m pip install -r requirements`
This will install external libraries required by the auto updater

## Configuration
The configuration options for the updater are:
* steamcmd_location - the location to where you downloaded steamcmd*
* steam_api_key - steam api key for your developer [account](https://steamcommunity.com/dev/apikey)*
* version_file - file name to store the current version of the game server
* Games - this is an array of Game Servers that you would like to run*
  * app_id - the [app id](https://steamdb.info/) of the game to be updated
  * game_name - name of the game to be checked, for loggin purposes
  * game_dir - directory of the executable to be ran to start the game server*
  * game_exe - name of the file that starts the game server*
  * steamcmd_exe - name of the file that starts steamcmd to check for updates*
  * process_name - name of the process that runs the game server*

note: * means this option needs to be changed before first use
`steamcmd_location`, `steam_api_key`, `version_file`, can all be overwritten in the game settings, if they are not present then the updater will revert to using the global values

### Running
In the repo directory, run:
`python .` or `python __main__.py`
This will check the configured games for updates, stop them, update them, and then restart them

### Scheduling
This updater is intended to be run automatically, some examples of methods groupped by os:
* Windows - Task Scheduler
* Linux - crontab 
