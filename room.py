from player import *

class Room:
    def __init__(self):
        self.players = []
        self.chatting = False

    def is_chatting(self):
        return self.chatting

    def set_chatting(self, isChatting):
        self.chatting = isChatting

    def add_player(self):
        self.players.append(Player(self))

    def pop_player(self):
        self.players[-1].delete()
        self.players.pop()

    def draw(self):
        for player in self.players:
            player.draw()

    def update(self, data):
        if(data[:3] == "000"):
            data = data[3:].split('@')
            while(len(self.players) < len(data) - 1):
                self.add_player()
            while (len(self.players) > len(data) - 1):
                self.pop_player()
            for i in range(len(data)):
                if data[i]:
                    temp = data[i].split('*')
                    self.players[i].set_pos((temp[0], temp[1]))
                    self.players[i].state = int(temp[2])

    def enable_chat(self):
        self.set_chatting(True)
        chat.config(state='normal')
        chat.focus_set()

    def disable_chat(self):
        self.set_chatting(False)
        chat.delete('1.0', END)
        chat.config(state='disabled')
        screen.focus_set()
