import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
print(f'We have connected to the server')

while True:
    message = input()
    sock.send(message.encode())
    print('Sending this message')
    data = sock.recv(1024)
    print(f'Receiving a message => {data.decode()}')
    if message == 'exit':
        print(f'We have been disconnected to the server')
        sock.close()
        break
