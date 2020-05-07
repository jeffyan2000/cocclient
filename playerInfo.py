import json
from os import path

name = input("enter your name: ")

is_correct_skin = False
while not is_correct_skin:
    skin = input("enter your skin name(png): ")
    if path.exists(path.join("lib", "characters", skin+".png")):
        is_correct_skin = True
    else:
        print("skin does not exist")

data = {}
data['info'] = []
data['info'].append({
    'name': name,
    'skin': skin
})

with open('player_info.json', 'w') as outfile:
    json.dump(data, outfile)
