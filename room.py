from player import *

class Room:
    def __init__(self):
        self.players = {}
        self.chatting = False
        self.my_x, self.my_y = 0, 0

    def is_chatting(self):
        return self.chatting

    def set_chatting(self, isChatting):
        self.chatting = isChatting

    def add_player(self, id):
        self.players[id] = Player(self, id)

    def pop_player(self, id):
        self.players[id].delete()

    def draw(self):
        for player in self.players:
            self.players[player].draw()

    def update(self, data):
        if data[:3] == "000":
            data = data[3:].split('@')
            for i in range(len(data)):
                if data[i]:
                    temp = data[i].split('*')
                    if temp[0] == IDS["id"]:
                        self.my_x = int(temp[1])
                        self.my_y = int(temp[2])
                    if temp[0] not in self.players:
                        self.add_player(temp[0])
                    self.players[temp[0]].set_pos((temp[1], temp[2]))
                    self.players[temp[0]].state = int(temp[3])

            for player in self.players:
                self.players[player].move((-self.my_x+screen_offset[0], -self.my_y+screen_offset[1]))

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
