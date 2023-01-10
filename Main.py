import os
from pystyle import *
import json
from rich import print_json
import getpass
from elevate import elevate
from time import sleep
from colorama import *
import errors

## elevate()



username = getpass.getuser()

user_directory_path = f'C:/Users/{username}'


os.system('cls')

done = False


banner = '''
     ___                             __    __     
    /   |  _____________  ____ ___  / /_  / /_  __
   / /| | / ___/ ___/ _ \/ __ `__ \/ __ \/ / / / /
  / ___ |(__  |__  )  __/ / / / / / /_/ / / /_/ / 
 /_/  |_/____/____/\___/_/ /_/ /_/_.___/_/\__, /  
                                         /____/   

'''

print(Colorate.Color(Colors.purple, banner, True))


print(Colorate.Color(Colors.green, ' reading "config.json"...\n'))


setup_type = open('config.json')

data = json.load(setup_type)


if data["setup_type"] == 'full':
    print_json(data=data)
    print('')
    ##sleep(2)

    '''
    Installation of Chocolatey the package manager for Windows
    
    '''
    os.system("powershell -command Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))")


'''
Install Chrome or FireFox depending on which one is in the "search_engine" field.

If empty error will be declared.

'''
if data["search_engine"] != 'chrome' or data["search_engine"] != 'firefox':
    setup_type = open('config.json')
    print_json(data=data)
    print('')
    print(Colorate.Color(Colors.red, 'Field "search_engine" can not be empty...', True))
    errors.search_engine()
elif data["search_engine"] == 'chrome':
    print(Colorate.Color(Colors.purple, 'Installing Google Chrome...', True))
    os.system('choco install googlechrome -y --force')

elif data["search_engine"] == 'firefox':
    print(Colorate.Color(Colors.purple, 'Installing FireFox...', True))
    os.system('choco install firefox -y --force')

        


        
        


    '''
    The below will retrieve the Latest SpotX Installation of spotify and install it to PC

    Everyone Likes Music Dont they...
    
    
    print(Colorate.Color(Colors.purple, ' Installing Spotify (No Ads)...', True))
    os.system('curl -L -O https://github.com/SpotX-CLI/SpotX-Win/releases/download/1.7/Install.bat')
    os.system(f'Install.bat')
    os.remove('Install.bat')
    '''

    


else:
    print_json(data=data)
    print('')
    print(Colorate.Color(Colors.purple, ' String should = full or essential or custom\n'))
    print(Colorate.Color(Colors.red, ' Press Enter To Exit\n'))
    input('')
    
