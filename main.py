from game import *

game = Game()
game.room = Room()

@sio.event
def connect():
    print('connection established')
    sio.emit('info', "Hello tcp")
    sio.emit('port', UDP_PORT_RECEIVE)

@sio.event
def message(data):
    print('message received with ', data)

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://{}:{}'.format(HOST_IP, TCP_PORT_SEND))

class sock_rec_syn_class(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
        self.dead = False

    def run(self):
        print("udp listening at " + str(UDP_PORT_RECEIVE))
        sock_receive.sendto(bytes("Hello udp", "utf-8"), (HOST_IP, UDP_PORT_SEND))
        while not self.dead:
            data, addr = sock_receive.recvfrom(1024)
            game.update_room(data.decode('ascii'))

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
