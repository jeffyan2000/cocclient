from player import*
from room import *

evt = EventHandler()

room = Room()

@sio.event
def connect():
    print('connection established')
    sio.emit('info', "Hello tcp")

@sio.event
def my_message(data):
    print('message received with ', data)
    sio.emit('my response', {'response': 'my response'})

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://localhost:{}'.format(TCP_PORT_SEND))

class sock_rec_syn_class(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
        self.dead = False

    def run(self):
        # udp receiver socket
        sock_receive = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock_receive.bind((UDP_IP, UDP_PORT_RECEIVE))
        print("udp listening")
        while not self.dead:
            data, addr = sock_receive.recvfrom(1024)
            print("Message: " + data.decode('ascii'))
        sock_receive.close()

    def stop(self):
        self.dead = True

sock_rec_syn_thread = sock_rec_syn_class()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sock_rec_syn_thread.stop()
            sio.disconnect()
            sock_send.close()
            pygame.quit()
            sys.exit()
        evt.handle_event(event)
    clock.tick(20)
