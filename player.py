from config import *

class Player:
    def __init__(self, room, id):
        self.room = room
        self.pos = [0, 0]
        self.previous_state = 0
        self.state = 0
        self.texture = "default_frames"
        self.size = (77, 77)
        self.frames = (8, 4)
        self.image = screen.create_image(0, 0, image=animation_lib[self.texture][0], anchor=NW)
        self.id = id

        self.speech = screen.create_text(int(player_deme[0]/2), -20, justify=CENTER, text="testesttestesttestesttestesttestesttestest", width=80)
        self.speech_start_time = 0
        self.speech_total_time = 0

    def start_speech(self, text):
        screen.itemconfig(self.speech, text=text)

    def set_pos(self, pos):
        dx, dy = int(pos[0]) - self.pos[0], int(pos[1]) - self.pos[1]
        self.move((dx, dy))
        if self.state != self.previous_state:
            self.previous_state = self.state
            screen.itemconfig(self.image, image=animation_lib[self.texture][self.state])

    def move(self, pos):
        screen.move(self.image, pos[0], pos[1])
        screen.move(self.speech, pos[0], pos[1])
        self.pos[0] += int(pos[0])
        self.pos[1] += int(pos[1])

    def delete(self):
        screen.delete(self.image)
        screen.delete(self.speech)
        del self.room.players[self.id]
