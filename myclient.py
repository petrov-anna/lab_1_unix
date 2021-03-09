import socket

sock = socket.socket()
sock.connect(('localhost', 9999))
mes = input("Write a message ")
sock.send(mes.encode())

data = sock.recv(1024)
sock.close()

print(data.decode())

