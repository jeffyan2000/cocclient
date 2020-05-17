from room import *
from gui import *

key_is_pressed = {}

class Game:
    def __init__(self):
        window.bind('<KeyRelease>', self.handleKeyPressed)
        window.bind('<KeyPress>', self.handleKeyPressed)
        window.bind('<Button-1>', self.handleMousePressed)
        window.bind('<ButtonRelease-1>', self.handleMouseReleased)
        self.room = None
        window.after(50, self.update)
        self.gui = None

    def showGuiBackpack(self):
        if self.gui is None:
            self.gui = BackpackGui()
            self.gui.show()
            self.gui.put_item(0, Item(2, "toolshovel"))
            self.gui.put_item(1, Item(1, "toolpickaxe"))

    def closeGuiBackpack(self):
        if self.gui:
            self.gui.close()
            self.gui = None

    def handleMousePressed(self, event):
        if self.gui:
            self.gui.onClick(event)

    def handleMouseReleased(self, event):
        if self.gui:
            self.gui.onRelease(event)

    def update(self):
        self.room.update_players()
        self.room.update_items()
        if self.gui:
            self.gui.update()
        window.after(200, self.update)

    def update_room(self, data):
        self.room.update(data)

    def handleKeyPressed(self, evt):
        if self.room.is_chatting():
            text = chat.get("1.0", END)
            if len(text) > WORD_LIMIT + 1:
                chat.delete(1.0, END)
                chat.insert(END, text[:WORD_LIMIT])
        if self.room is not None:
            is_pressed = None
            if str(evt.type) == "KeyPress":
                if evt.char not in key_is_pressed:
                    key_is_pressed[evt.char] = True
                    is_pressed = 1
                else:
                    if key_is_pressed[evt.char] == False:
                        is_pressed = 1
                        key_is_pressed[evt.char] = True

            elif str(evt.type) == "KeyRelease":
                key_is_pressed[evt.char] = False
                is_pressed = 0

            if is_pressed is not None:
                # player movement
                if not self.room.is_chatting():
                    if evt.char == 'w':
                        sio.emit("keyPressed", "1"+str(is_pressed))
                    elif evt.char == 'a':
                        sio.emit("keyPressed", "2"+str(is_pressed))
                    elif evt.char == 's':
                        sio.emit("keyPressed", "3"+str(is_pressed))
                    elif evt.char == 'd':
                        sio.emit("keyPressed", "4"+str(is_pressed))
                    #switch to chat
                    elif not is_pressed and evt.char == 't':
                        self.room.enable_chat()
                    #open backpack
                    elif evt.char == 'b' and is_pressed:
                        if self.gui:
                            self.closeGuiBackpack()
                        else:
                            self.showGuiBackpack()

                elif evt.keycode == 13:
                    msg = chat.get("1.0", END)
                    sio.emit("speech", msg[:-1].encode("UTF-8"))
                    self.room.disable_chat()
