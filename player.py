from config import *

class Player:
    def __init__(self, room, id, name, skin):
        self.room = room
        self.pos = [0, 0]
        self.previous_state = 0
        self.state = 0
        self.name = name
        self.texture = skin + "_frames"
        self.size = (77, 77)
        self.frames = (8, 4)
        self.image = screen.create_image(0, 0, image=animation_lib[self.texture][0], anchor=NW)
        self.id = id

        self.current_text = ""
        self.bubble = None
        self.speech = None
        self.speech_start_time = 0
        self.speech_total_time = 0

    def start_speech(self, text):
        self.stop_speech()
        size = arial14.measure(text)
        if size > 300:
            size = 300
        self.bubble = screen.create_rectangle(int(player_deme[0] / 2) - size/2 - 5 + self.pos[0],
                                              -55 + self.pos[1], int(player_deme[0] / 2) + self.pos[0] + size/2 + 5,
                                              5 + self.pos[1],
                                              fill="#FFFFFF")
        self.speech = screen.create_text(int(player_deme[0] / 2) + self.pos[0],
                                         -25 + self.pos[1], font=arial14, justify=CENTER,
                                         text=text, width=300)

        screen.itemconfig(self.speech, text=text)
        self.current_text = text
        self.speech_start_time = time.time()
        self.speech_total_time = arial14.measure(text)/50

    def stop_speech(self):
        screen.delete(self.speech)
        screen.delete(self.bubble)
        self.current_text = ""

    def update(self):
        if self.current_text:
            if time.time() - self.speech_start_time > self.speech_total_time:
                self.stop_speech()


    def set_pos(self, pos):
        dx, dy = int(pos[0]) - self.pos[0], int(pos[1]) - self.pos[1]
        self.move((dx, dy))
        if self.state != self.previous_state:
            self.previous_state = self.state
            screen.itemconfig(self.image, image=animation_lib[self.texture][self.state])

    def move(self, pos):
        if self.speech and self.bubble:
            screen.move(self.speech, pos[0], pos[1])
            screen.move(self.bubble, pos[0], pos[1])
        screen.move(self.image, pos[0], pos[1])
        self.pos[0] += int(pos[0])
        self.pos[1] += int(pos[1])

    def delete(self):
        screen.delete(self.image)
        screen.delete(self.speech)
        del self.room.players[self.id]
