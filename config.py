import pygame, sys, threading, os
from threading import Thread

pygame.init()

screen_width, screen_height = 400, 400

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

import socket
import socketio

#udp receiving port
UDP_PORT_RECEIVE = 5005
#udp sending port
UDP_PORT_SEND = 41234
#tcp sending port
TCP_PORT_SEND = 5006
#destination IP
UDP_IP = "localhost"

#udp sender socket
message = "Hello udp"
sock_send = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_send.sendto(bytes(message, "utf-8"), (UDP_IP, UDP_PORT_SEND))


sio = socketio.Client()

def load(n):
    return pygame.image.load(os.path.join("lib", "texture") + n + ".png").convert_alpha()

texture_names = ["default"]

texture_lib = {}
for name in texture_names:
    texture_lib[name] = load(name)
def add_left(names):
    for name in names:
        texture_lib[name+"_left"] = pygame.transform.flip(texture_lib[name], True, False)
