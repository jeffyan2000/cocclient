import pygame, sys, threading, os, random, time
from threading import Thread

pygame.init()

screen_width, screen_height = 400, 400

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

import socket
import socketio

#udp receiving port
UDP_PORT_RECEIVE = random.randint(7000, 8000)
#udp sending port
UDP_PORT_SEND = 6002
#tcp sending port
TCP_PORT_SEND = 6001
#destination IP vps197548.vps.ovh.ca
HOST_IP = "vps197548.vps.ovh.ca"

#udp sender socket
# udp receiver socket
sock_receive = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_receive.bind(("0.0.0.0", UDP_PORT_RECEIVE))

sio = socketio.Client()

def load(n):
    return pygame.image.load(os.path.join("lib", "characters", n + ".png")).convert_alpha()

texture_names = ["default"]

texture_lib = {}
for name in texture_names:
    texture_lib[name] = load(name)
def add_left(names):
    for name in names:
        texture_lib[name+"_left"] = pygame.transform.flip(texture_lib[name], True, False)
