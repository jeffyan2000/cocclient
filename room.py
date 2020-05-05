from player import *

class Room:
    def __init__(self):
        self.players = []

    def draw(self):
        for player in self.players:
            player.draw()

    def update(self, data):
        if(data[:3] == "000"):
            data = data[3:].split('@')
            while(len(self.players) < len(data) - 1):
                self.players.append(Player())
            while (len(self.players) > len(data) - 1):
                self.players[-1].delete()
                self.players.pop()
            for i in range(len(data)):
                if data[i]:
                    temp = data[i].split('*')
                    self.players[i].set_pos((temp[0], temp[1]))
                    self.players[i].state = int(temp[2])

