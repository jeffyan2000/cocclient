import sys, threading, os, random, time
from tkinter import *
from PIL import Image, ImageTk
from threading import Thread

screen_width, screen_height = 400, 400

window = Tk()
window.title("test")


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

sio = socketio.Client()

image_lib = {}
def load(n):
    img = Image.open(os.path.join("lib", "characters", n + ".png"))
    image_lib[name] = img
    return ImageTk.PhotoImage(img)

texture_names = ["default"]

texture_lib = {}
animation_lib = {}
for name in texture_names:
    texture_lib[name] = load(name)

def loadFrames(name, size, frames):
    animation_lib[name+"_frames"] = []
    for y in range(frames[1]):
        for x in range(frames[0]):
            cropped = image_lib[name].crop((x * size[0], y * size[1], (x+1) * size[0], (y+1) * size[1]))
            animation_lib[name+"_frames"].append(ImageTk.PhotoImage(cropped))

loadFrames("default", (77, 77), (8, 4))

class GCanvas(Canvas):
    def __init__(self):
        Canvas.__init__(self, window, width=screen_width, height=screen_height, background="#FFFFFF")
        self.after(40, self.onTimer)

    def onTimer(self):
        self.after(40, self.onTimer)



screen = GCanvas()

titles = {"chat":Label(window, text="Press [T] to Chat, [Return] to finish typing"),
        "name":Label(window, text="CocTool Alpha")}

chat = Text(width=int(screen_width/8), height=int(screen_height/40), wrap=WORD, background="#FFFFFF")
chat.config(state='disabled')

screen.pack(fill=BOTH, expand=1)
titles["chat"].pack()
chat.pack(fill=BOTH, expand=1)

screen.focus_set()