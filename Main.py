import os
from pystyle import *
import json
from rich import print_json
import getpass
from elevate import elevate

elevate()
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
    print('')
    print(Colorate.Color(Colors.purple, ' Installing Spotify (No Ads)...', True))
    os.system('curl -L -O https://github.com/SpotX-CLI/SpotX-Win/releases/download/1.7/Install.bat')
    os.system(f'Install.bat')
    os.remove('Install.bat')

    os.system("powershell -command Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))")

    applications = '''
    choco install visualstudiocode -y
    choco install slack -y
    choco install pandoc -y
    
    
    choco install git -y
    choco install github -y -ignore-checksums
    
     
    choco install docker-desktop -y
    choco install terraform -y
    choco install chefdk -y
    choco install packer -y
    choco install vagrant -y
    
     
    choco install kubernetes-cli -y
    choco install kubernetes-helm -y
    choco install minikube -y
    choco install eksctl -y
    
     
    choco install azure-data-studio -y
    choco install sql-server-management-studio -y
    
    
    choco install putty -y
    choco install mremoteng -y
    
     
    choco install azure-cli -y
    choco install awscli -y
    
    
    choco install python3 -y
    choco install pip -y
    
    
    pip install pre-commit
    pip install terrascan
    
        
        
    '''
    os.system(applications)
    

elif data["setup_type"] == 'essential':
    print('')

elif data["setup_type"] == 'custom':
    print('')


else:
    print_json(data=data)
    print('')
    print(Colorate.Color(Colors.purple, ' String should = full or essential or custom\n'))
    print(Colorate.Color(Colors.red, ' Press Enter To Exit\n'))
    input('')
    
