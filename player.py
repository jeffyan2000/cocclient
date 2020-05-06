from config import *

class Player:
    def __init__(self, room):
        self.room = room
        self.pos = [0, 0]
        self.previous_state = 0
        self.state = 0
        self.texture = "default_frames"
        self.size = (77, 77)
        self.frames = (8, 4)
        self.image = screen.create_image(0, 0, image=animation_lib[self.texture][0], anchor=NW)

        self.speeches = []

    def set_pos(self, pos):
        dx, dy = int(pos[0]) - self.pos[0], int(pos[1]) - self.pos[1]
        screen.move(self.image, dx, dy)
        self.pos[0] = int(pos[0])
        self.pos[1] = int(pos[1])
        if self.state != self.previous_state:
            self.previous_state = self.state
            screen.itemconfig(self.image, image=animation_lib[self.texture][self.state])

    def delete(self):
        screen.delete(self.image)
