from config import *

class Gui:
    def __init__(self):
        self.pos = [0, 0]
        self.grabbed = False
        self.clicked_pos = [0, 0]
        self.grab_rect = (86, 34, 159, 46)

    def show(self):
        pass

    def onClick(self, event):
        if self.grab_rect[2] + self.pos[0] > mouse_pos[0] > self.grab_rect[0] + self.pos[0]:
            if self.grab_rect[3] + self.pos[1] > mouse_pos[1] > self.grab_rect[1] + self.pos[1]:
                self.clicked_pos[0] = event.x - self.pos[0]
                self.clicked_pos[1] = event.y - self.pos[1]
                self.grabbed = True

    def onRelease(self, event):
        self.grabbed = False

    def update(self):
        if self.grabbed:
            self.set(mouse_pos[0] - self.clicked_pos[0], mouse_pos[1] - self.clicked_pos[1])


    def set(self, x, y):
        dx, dy = x - self.pos[0], y - self.pos[1]
        self.move(dx, dy)

    def move(self, dx, dy):
        self.pos[0] += dx
        self.pos[1] += dy

class BackpackGui(Gui):
    def __init__(self):
        Gui.__init__(self)
        self.pos[0] = 350
        self.pos[1] = 0
        self.bg_image = None
        self.slots = []

    def move(self, dx, dy):
        Gui.move(self, dx, dy)
        for slot in self.slots:
            screen.move(slot, dx, dy)
        screen.move(self.bg_image, dx, dy)

    def show(self):
        self.bg_image = screen.create_image(self.pos[0], self.pos[1], anchor="nw", image=gui_lib["backpack_bg"])
        screen.tag_raise(self.bg_image)

        for x in range(4):
            self.slots.append(screen.create_image(self.pos[0] + x * 40 + 49, 269,
                                anchor="nw", image=gui_lib["slot"]))
            screen.tag_raise(self.slots[-1])

        for y in range(5):
            for x in range(4):
                self.slots.append(screen.create_image(self.pos[0] + x*40 + 49, self.pos[1] + 45 + y*40,
                                    anchor="nw", image=gui_lib["slot"]))
                screen.tag_raise(self.slots[-1])


