from room import *

evt = EventHandler()

room = Room()

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
            room.update(data.decode('ascii'))

    def stop(self):
        self.dead = True

sock_rec_syn_thread = sock_rec_syn_class()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sock_rec_syn_thread.stop()
            sio.disconnect()
            sock_receive.close()
            pygame.quit()
            sys.exit()
        evt.handle_event(event)

    screen.fill(-1)
    room.draw()
    pygame.display.flip()
    clock.tick(40)
