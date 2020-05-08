from player import *

class Room:
    def __init__(self):
        self.players = {}
        self.chatting = False
        self.my_x, self.my_y = 0, 0
        self.background = screen.create_image(270, 220, image=background_lib["default"])

    def set_pos(self, pos):
        dx, dy = pos[0] - self.my_x, pos[1] - self.my_y
        if dx or dy:
            screen.move(self.background, dx, dy)
            self.my_x = pos[0]
            self.my_y = pos[1]

    def is_chatting(self):
        return self.chatting

    def set_chatting(self, isChatting):
        self.chatting = isChatting

    def add_player(self, id, pname, skin):
        self.players[id] = Player(self, id, pname, skin)

    def pop_player(self, id):
        self.players[id].delete()

    def draw(self):
        for player in self.players:
            self.players[player].draw()

    def update_players(self):
        for player in self.players:
            self.players[player].update()

    def update(self, data):
        if data[:3] == "000":
            data = data[3:].split('@')
            for i in range(len(data)):
                if data[i]:
                    temp = data[i].split('*')
                    if temp[0] == "!":
                        self.set_pos((-int(temp[1]), -int(temp[2])))
                    elif temp[0] in self.players:
                        self.players[temp[0]].set_pos((int(temp[1])+screen_offset[0], int(temp[2])+screen_offset[1]))
                        self.players[temp[0]].state = int(temp[3])
            screen.update()

        elif data[:3] == "001":
            self.players[data[3:5]].start_speech(data[5:])

    def enable_chat(self):
        self.set_chatting(True)
        chat.config(state='normal')
        chat.focus_set()

    def disable_chat(self):
        self.set_chatting(False)
        chat.delete('1.0', END)
        chat.config(state='disabled')
        screen.focus_set()
