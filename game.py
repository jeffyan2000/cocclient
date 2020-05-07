from room import *

key_is_pressed = {}

class Game:
    def __init__(self):
        window.bind('<KeyRelease>', self.handleKeyPressed)
        window.bind('<KeyPress>', self.handleKeyPressed)
        self.room = None

    def update_room(self, data):
        self.room.update(data)

    def handleKeyPressed(self, evt):
        if self.room is not None:
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

            if is_pressed is not None:
                # player movement
                if not self.room.is_chatting():
                    if evt.char == 'w':
                        sio.emit("keyPressed", ["1", is_pressed])
                    elif evt.char == 'a':
                        sio.emit("keyPressed", ["2", is_pressed])
                    elif evt.char == 's':
                        sio.emit("keyPressed", ["3", is_pressed])
                    elif evt.char == 'd':
                        sio.emit("keyPressed", ["4", is_pressed])
                    #switch to chat
                    elif not is_pressed and evt.char == 't':
                        self.room.enable_chat()

                elif evt.keycode == 13:
                    msg = chat.get("1.0", END)
                    sio.emit("speech", msg[:-1])
                    self.room.disable_chat()
