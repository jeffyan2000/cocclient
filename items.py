from config import *

class Item:
    def __init__(self, iid, texture, name=None):
        self.id = iid
        self.dropped = False
        self.pos = [0, 0]
        self.image = None
        self.size = (32, 32)
        self.texture = item_lib[texture]
        self.item_name_image = None
        self.name = texture
        if name:
            self.name = name

    def showName(self):
        self.name = screen.create_text(self.pos[0]+self.size[0]/2, self.pos[1]-10, text=self.name)

    def hideName(self):
        screen.delete(self.name)
        self.name = None

    def getdistance(self, player):
        return (abs(player.pos[0] + player_deme[0]/2 - self.pos[0] - self.size[0]/2)
                + abs(player.pos[1] + player_deme[1]/2 - self.pos[1] - self.size[1]/2))/2

    def drop(self, pos):
        self.pos[0] = pos[0]
        self.pos[1] = pos[1]
        self.image = screen.create_image(self.pos[0], self.pos[1], image=self.texture, anchor=NW)
        self.dropped = True

    def move(self, dx, dy):
        if self.image:
            self.pos[0] += dx
            self.pos[1] += dy
            screen.move(self.image, dx, dy)
            if self.item_name_image:
                screen.move(self.item_name_image, dx, dy)

    def pick(self):
        screen.delete(self.image)
        self.image = None

class BackPack:
    def __init__(self, row):
        self.row = row
        self.items = [[None, None, None, None, None] for _ in range(row)]



