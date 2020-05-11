from config import *

class Item:
    def __init__(self, iid, texture):
        self.id = iid
        self.dropped = False
        self.pos = [0, 0]
        self.image = None
        self.size = (32, 32)
        self.texture = item_lib[texture]

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

    def pick(self):
        screen.delete(self.image)
        self.image = None

class BackPack:
    def __init__(self, row):
        self.row = row
        self.items = [[None, None, None, None, None] for _ in range(row)]



