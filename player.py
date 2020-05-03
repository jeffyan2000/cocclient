from config import *

class Player():
    def __init__(self, id):
        self.id = id
        self.pos = [0, 0]

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
