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

print(banner)

print(Colorate.Color(Colors.green, ' reading "config.json"...\n'))


setup_type = open('config.json')

data = json.load(setup_type)


print_json(data=data)
