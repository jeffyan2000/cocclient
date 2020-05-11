from game import *

game = Game()
game.room = Room()

@sio.event
def connect():
    print('connection established')
    sio.emit('info', IDS["name"] + "@" + IDS["skin"])
    sio.emit('port', UDP_PORT_RECEIVE)

@sio.event
def message(data):
    print('message received with ', data)\

@sio.event
def id(data):
    print('My id is ', data)
    IDS["id"] = data

@sio.event
def new_player(data):
    temp = data.split("@")
    game.room.add_player(temp[2], temp[0], temp[1])

@sio.event
def remove_player(data):
    game.room.players[data].delete()

@sio.event
def new_players(data):
    print(data)
    temp = data.split("@")
    for item in temp:
        if item:
            temp2 = item.split("*")
            print(temp2)
            game.room.add_player(temp2[2], temp2[0], temp2[1])

@sio.event
def sync_dict(data):
    print('message received with ', data)\

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://{}:{}'.format(HOST_IP, TCP_PORT_SEND))

class sock_rec_syn_class(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.dead = False
        self.start()

    def run(self):
        print("udp listening at " + str(UDP_PORT_RECEIVE))
        sock_receive.sendto(bytes("Hello udp", "utf-8"), (HOST_IP, UDP_PORT_SEND))
        while not self.dead:
            if IDS["id"] is not None:
                data, addr = sock_receive.recvfrom(1024)
                game.update_room(data.decode('utf-8'))

    def stop(self):
        self.dead = True

sock_rec_syn_thread = sock_rec_syn_class()

def on_closing():
    sock_rec_syn_thread.stop()
    sio.disconnect()
    sock_receive.close()
    window.destroy()
    sys.exit()

window.protocol("WM_DELETE_WINDOW", on_closing)



window.mainloop()
