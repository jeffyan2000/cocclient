import socket
import socketio

#udp receiving port
UDP_PORT_RECEIVE = 5005
#udp sending port
UDP_PORT_SEND = 41234
#tcp sending port
TCP_PORT_SEND = 5006
#destination IP
UDP_IP = "localhost"

#udp sender socket
message = "Hello udp"
sock_send = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_send.sendto(bytes(message, "utf-8"), (UDP_IP, UDP_PORT_SEND))

#udp receiver socket
sock_receive = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_receive.bind((UDP_IP, UDP_PORT_RECEIVE))
print("udp listening")


sio = socketio.Client()
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
sio.wait()

while True:
    data, addr = sock_receive.recvfrom(1024) # buffer size is 1024 bytes
    print(data.decode("utf-8"))
