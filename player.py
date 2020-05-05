from config import *

class Player:
    def __init__(self):
        self.pos = [0, 0]
        self.previous_state = 0
        self.state = 0
        self.texture = "default_frames"
        self.size = (77, 77)
        self.frames = (8, 4)
        self.image = screen.create_image(0, 0, image=animation_lib[self.texture][0], anchor=NW)

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


key_is_pressed = {}
def handleKeyPressed(evt):
    is_pressed = None
    if str(evt.type) == "KeyPress":

        if evt.char not in key_is_pressed:
            key_is_pressed[evt.char] = True
            is_pressed = True
        else:
            if key_is_pressed[evt.char] == False:
                is_pressed = True
                key_is_pressed[evt.char] = True

    elif str(evt.type) == "KeyRelease":
        key_is_pressed[evt.char] = False
        is_pressed = False
    if  is_pressed is not None:
        if evt.char == 'w':
            sio.emit("keyPressed", ["1", is_pressed])
        elif evt.char == 'a':
            sio.emit("keyPressed", ["2", is_pressed])
        elif evt.char == 's':
            sio.emit("keyPressed", ["3", is_pressed])
        elif evt.char == 'd':
            sio.emit("keyPressed", ["4", is_pressed])

window.bind('<KeyRelease>', handleKeyPressed)
window.bind('<KeyPress>', handleKeyPressed)