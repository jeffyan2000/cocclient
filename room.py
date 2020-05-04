from config import *

class Room:
    def __init__(self):
        self.players = []

    def draw(self):
        for player in self.players:
            player.draw()
