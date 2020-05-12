from config import *

class Gui:
    def __init__(self):
        self.pos = [0, 0]

    def show(self):
        pass

class BackpackGui(Gui):
    def __init__(self):
        Gui.__init__(self)
        self.pos[0] = 350
        self.pos[1] = 0

    def show(self):
        screen.create_image(self.pos[0], self.pos[1], anchor="nw", image=gui_lib["backpack_bg"])
        for y in range(5):
            for x in range(4):
                screen.create_image(self.pos[0] + x*40 + 49, self.pos[1] + 45 + y*40,
                                    anchor="nw", image=gui_lib["slot"])
        for x in range(4):
            screen.create_image(self.pos[0] + x * 40 + 49, 269,
                                anchor="nw", image=gui_lib["slot"])
