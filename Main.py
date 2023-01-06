import os
from pystyle import *
import json
from rich import print_json

os.system('cls')


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

if data["setup_type"] != 'default' or data["setup_type"] != 'full' or data["setup_type"] != 'essential' or data["setup_type"] != 'custom':
    print_json(data=data)
    print('')
    print(Colorate.Color(Colors.purple, ' String should = default or full or essential or custom\n'))
