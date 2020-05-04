from config import *

class Player:
    def __init__(self):
        self.pos = [0, 0]
        self.stat = 0
        self.texture = "default"
        self.size = (77, 77)
        self.frames = (8, 4)
        self.rects = [pygame.Rect((x * self.size[0], y * self.size[1]), self.size)
                      for x in range(self.frames[0])
                      for y in range(self.frames[1])]

    def set_pos(self, pos):
        self.pos[0] = int(pos[0])
        self.pos[1] = int(pos[1])

    def draw(self):
        screen.blit(texture_lib[self.texture], self.pos,  self.rects[self.stat])

class EventHandler():
    def handle_event(self, event):
        is_pressed = None
        if event.type == pygame.KEYDOWN:
            is_pressed = True
        elif event.type == pygame.KEYUP:
            is_pressed = False
        if  is_pressed is not None:
            if event.key == pygame.K_w:
                sio.emit("keyPressed", ["1", is_pressed])
            elif event.key == pygame.K_a:
                sio.emit("keyPressed", ["2", is_pressed])
            elif event.key == pygame.K_s:
                sio.emit("keyPressed", ["3", is_pressed])
            elif event.key == pygame.K_d:
                sio.emit("keyPressed", ["4", is_pressed])
