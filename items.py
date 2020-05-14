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
        self.item_name_bg = None
        self.name = texture
        if name:
            self.name = name
        self.name_size = arial15.measure(self.name) + 10
        self.name_rect = (-self.name_size/2, -21, self.name_size/2, -43)

    def showName(self):
        self.item_name_bg = screen.create_rectangle(self.pos[0] + self.name_rect[0],
                                                    self.pos[1] + self.name_rect[1],
                                                    self.pos[0] + self.name_rect[2],
                                                    self.pos[1] + self.name_rect[3], fill="#ffffff")
        self.item_name_image = screen.create_text(self.pos[0],
                                                  self.pos[1]-self.size[1],
                                                  text=self.name,
                                                  font=arial15)

    def hideName(self):
        screen.delete(self.item_name_image)
        screen.delete(self.item_name_bg)
        self.item_name_image = None
        self.item_name_bg = None

    def getDistance(self, pos):
        return (abs(pos[0] + player_deme[0]/2 - self.pos[0])
                + abs(pos[1] + player_deme[1] - self.pos[1]))/2

    def create_image(self, pos):
        self.pos[0] = pos[0]
        self.pos[1] = pos[1]
        self.image = screen.create_image(self.pos[0], self.pos[1], image=self.texture)

    def move(self, dx, dy):
        if self.image:
            self.pos[0] += dx
            self.pos[1] += dy
            screen.move(self.image, dx, dy)
            if self.item_name_image:
                screen.move(self.item_name_image, dx, dy)
            if self.item_name_bg:
                screen.move(self.item_name_bg, dx, dy)

    def set_pos(self, pos):
        dx, dy = int(pos[0]) - self.pos[0], int(pos[1]) - self.pos[1]
        self.move(dx, dy)

    def pick(self):
        screen.delete(self.image)
        self.image = None

class BackPack:
    def __init__(self, row):
        self.row = row
        self.items = [[None, None, None, None, None] for _ in range(row)]



