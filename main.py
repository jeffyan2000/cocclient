import socket

UDP_IP = "localhost"
UDP_PORT = 41234
MESSAGE = "Hello, World!"

sock = socket.socket(socket.AF_INET, # Internet
             socket.SOCK_DGRAM) # UDP
sock.sendto(bytes(MESSAGE, "utf-8"), (UDP_IP, UDP_PORT))

UDP_PORT_RECEIVE = 5005

sock_rec = socket.socket(socket.AF_INET, # Internet
             socket.SOCK_DGRAM) # UDP

sock_rec.bind((UDP_IP, UDP_PORT_RECEIVE))

print("listening")
while True:
    data, addr = sock_rec.recvfrom(1024) # buffer size is 1024 bytes
    print(data.decode("utf-8"))
