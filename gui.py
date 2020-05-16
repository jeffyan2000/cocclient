from items import *

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
        self.grabbed_item = None
        self.item_deme = 32
        self.item_rects = []
        self.item_slot = []
        for x in range(4):
            self.item_rects.append((x * 40 + 49, 269, x * 40 + 49 + self.item_deme, 269 + self.item_deme))
            self.item_slot.append(None)

        for y in range(5):
            for x in range(4):
                self.item_rects.append((x*40 + 49, 45 + y*40, x*40 + 49 + self.item_deme, 45 + y*40 + self.item_deme))
                self.item_slot.append(None)

    def move(self, dx, dy):
        Gui.move(self, dx, dy)
        for slotindex in range(len(self.slots)):
            screen.move(self.slots[slotindex], dx, dy)
            if self.item_slot[slotindex] is not None:
                self.item_slot[slotindex].move(dx, dy)
        screen.move(self.bg_image, dx, dy)

    def put_item(self, slot, item):
        self.item_slot[slot] = item
        item.create_image((self.item_rects[slot][0] + self.pos[0] + item.size[0]/2,
                           self.item_rects[slot][1] + self.pos[1] + item.size[1]/2))

    def update(self):
        Gui.update(self)
        if self.grabbed_item:
            dx, dy = mouse_pos[0] - self.grabbed_item.pos[0], mouse_pos[1] - self.grabbed_item.pos[1]
            self.grabbed_item.move(dx, dy)

    def colliedItem(self, event):
        for index, rect in enumerate(self.item_rects):
            if rect[0] < event.x - self.pos[0] < rect[2]:
                if rect[1] < event.y - self.pos[1] < rect[3]:
                    return index
        return -1

    def onClick(self, event):
        Gui.onClick(self, event)
        temp_slot = self.colliedItem(event)
        if temp_slot != -1:
            if self.item_slot[temp_slot] is not None or self.grabbed_item is not None:
                sio.emit('backpackOperation', temp_slot)
                self.grabbed_item, self.item_slot[temp_slot] = self.item_slot[temp_slot], self.grabbed_item
                if self.item_slot[temp_slot] is not None:
                    self.item_slot[temp_slot].set_pos(
                        (self.item_rects[temp_slot][0] + self.pos[0] + self.item_slot[temp_slot].size[0] / 2,
                         self.item_rects[temp_slot][1] + self.pos[1] + self.item_slot[temp_slot].size[1] / 2))

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


