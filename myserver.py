import socket

sock = socket.socket()
print('Socket created')

s_port = 9090
sock.bind(('', s_port))
sock.listen(1)
conn, addr = sock.accept()
print(f'Socket binded to port {s_port}')

running = True

print(f'Client {addr} was connected')
while running:
    data = conn.recv(1024)
    if not data:
        print(f'Client {addr} was disconnected')
        break
    print(f'Received message: {data.decode()}')
    if data.decode() == 'exit':
        print('Server is closing')
        running = False
        conn.close()
        break
    print(f'Sending message: {data.decode()}')
    conn.send(data)