import sys, threading, os, random, time, json
from tkinter import *
from tkinter import font as tkFont
from PIL import Image, ImageTk
from threading import Thread

screen_width, screen_height = 400, 400
player_deme = (77, 77)

screen_offset = (int(screen_width/2 - player_deme[0]/2), int(screen_height/2 - player_deme[1]/2))

window = Tk()
window.title("test")

arial36 = tkFont.Font(family='Arial', size=36)
arial14 = tkFont.Font(family='Arial', size=9)


import socket
import socketio

#udp receiving port
UDP_PORT_RECEIVE = random.randint(7000, 8000)
#udp sending port
UDP_PORT_SEND = 6002
#tcp sending port
TCP_PORT_SEND = 6001
#destination IP vps197548.vps.ovh.ca
HOST_IP = "localhost"

#udp sender socket
# udp receiver socket
sock_receive = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_receive.bind(("0.0.0.0", UDP_PORT_RECEIVE))

speech_width = 20

sio = socketio.Client()

image_lib = {}
def load(path, n):
    img = Image.open(os.path.join(path, n + ".png"))
    image_lib[n] = img
    return ImageTk.PhotoImage(img)

def loadFrames(name, size, frames):
    animation_lib[name+"_frames"] = []
    for y in range(frames[1]):
        for x in range(frames[0]):
            cropped = image_lib[name].crop((x * size[0], y * size[1], (x+1) * size[0], (y+1) * size[1]))
            animation_lib[name+"_frames"].append(ImageTk.PhotoImage(cropped))

texture_lib = {}
animation_lib = {}
background_lib = {}

skins = os.listdir(os.path.join("lib", "characters"))

texture_names = []
background_names = ["default"]
for character_texture in skins:
    texture_names.append(character_texture[:-4])

for name in texture_names:
    texture_lib[name] = load(os.path.join("lib", "characters"), name)
for name in background_names:
    background_lib[name] = load(os.path.join("lib", "room", "floor"), name)

for character_texture in skins:
    loadFrames(character_texture[:-4], player_deme, (8, 4))

class GCanvas(Canvas):
    def __init__(self):
        Canvas.__init__(self, window, width=screen_width, height=screen_height, background="#FFFFFF")


screen = GCanvas()

titles = {"chat":Label(window, text="Press [T] to Chat, [Return] to finish typing"),
        "name":Label(window, text="CocTool Alpha")}

chat = Text(width=int(screen_width/8), height=int(screen_height/40), wrap=WORD, background="#FFFFFF")
chat.config(state='disabled')

screen.pack(fill=BOTH, expand=1)
titles["chat"].pack()
chat.pack(fill=BOTH, expand=1)

screen.focus_set()

with open('player_info.json') as f:
  my_info = json.load(f)

IDS = {"id":None, "name":my_info["info"][0]["name"], "skin":my_info["info"][0]["skin"]}

WORD_LIMIT = 100
