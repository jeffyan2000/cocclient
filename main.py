from player import*

evt = EventHandler()

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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sio.disconnect()
            pygame.quit()
            sys.exit()
        evt.handle_event(event)
    clock.tick(20)
