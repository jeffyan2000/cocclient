from player import *

class Room:
    def __init__(self):
        self.players = []

    def draw(self):
        for player in self.players:
            player.draw()

    def update(self, data):
        data = data.split('@')
        for i in range(len(data)):
            if data[i]:
                if i >= len(self.players):
                    self.players.append(Player())
                temp = data[i].split('-')
                self.players[i].set_pos((temp[0], temp[1]))

