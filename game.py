from room import *

key_is_pressed = {}

class Game:
    def __init__(self):
        window.bind('<KeyRelease>', self.handleKeyPressed)
        window.bind('<KeyPress>', self.handleKeyPressed)

        chat.bind('<KeyRelease>', self.handleKeyPressed_chat)
        self.room = None

    def update_room(self, data):
        self.room.update(data)

    def handleKeyPressed_chat(self, evt):
        if evt.keycode == 13:
            sio.emit("speech", chat.get("1.0", END))
            self.room.disable_chat()

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
