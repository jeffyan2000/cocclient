from player import *

class TriggerBlock:
    def __init__(self, x, y, texture):
        self.image = None
        self.pos = [x, y]
        self.texture = texture



class Room:
    def __init__(self):
        self.players = {}
        self.chatting = False
        self.my_x, self.my_y = 0, 0
        self.my_ox, self.my_oy = 0, 0
        self.dropped_items = {}
        self.background = screen.create_image(screen_offset[0], screen_offset[1], anchor="nw", image=background_lib["default"])

    def update_items(self):
        flag = False
        for itemKey in self.dropped_items:
            if self.dropped_items[itemKey].getDistance((self.my_ox+screen_offset[0],
                                                        self.my_oy+screen_offset[1])) < 25 and not flag:
                flag = True
                if not self.dropped_items[itemKey].item_name_image:
                    self.dropped_items[itemKey].showName()
            else:
                if self.dropped_items[itemKey].item_name_image:
                    self.dropped_items[itemKey].hideName()

    def drop_item(self, item, pos):
        temp = [0, 0]
        temp[0] = self.my_x + pos[0] + screen_offset[0] + player_deme[0]/2
        temp[1] = self.my_y + pos[1] + screen_offset[1] + player_deme[1]/2
        self.dropped_items[item.id] = item
        self.dropped_items[item.id].create_image(temp)
        self.dropped_items[item.id].dropped = True

    def set_pos(self, pos):
        dx, dy = pos[0] - self.my_x, pos[1] - self.my_y
        if dx or dy:
            screen.move(self.background, dx, dy)
            for itemKey in self.dropped_items:
                self.dropped_items[itemKey].move(dx, dy)
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
        tempmyxy = [0, 0]
        if data[:3] == "000":
            data = data[3:].split('@')
            for i in range(len(data)):
                if data[i]:
                    temp = data[i].split('*')
                    if temp[0] == "!":
                        tempmyxy[0] = -int(temp[1])
                        tempmyxy[1] = -int(temp[2])

                    elif temp[0] in self.players:
                        if temp[0] == IDS["id"]:
                            self.my_ox = int(temp[1])
                            self.my_oy = int(temp[2])
                        self.players[temp[0]].set_pos((int(temp[1])+screen_offset[0], int(temp[2])+screen_offset[1]))
                        self.players[temp[0]].state = int(temp[3])
            self.set_pos((tempmyxy[0] + self.my_ox, tempmyxy[1] + self.my_oy))
            screen.update()

        elif data[:3] == "001":
            self.players[data[3:5]].start_speech(data[5:])

        elif data[:3] == "100":
            temp = data[3:].split("@")
            self.drop_item(item_id_list[temp[0]], (int(temp[1]), int(temp[2])))

    def enable_chat(self):
        self.set_chatting(True)
        chat.config(state='normal')
        chat.focus_set()

    def disable_chat(self):
        self.set_chatting(False)
        chat.delete('1.0', END)
        chat.config(state='disabled')
        screen.focus_set()
