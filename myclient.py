import socket

sock = socket.socket()
sock.connect(('localhost', 9999))
sock.send("Hello World!".encode())

data = sock.recv(1024)
sock.close()

print(data.decode())

