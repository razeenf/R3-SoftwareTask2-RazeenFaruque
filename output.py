import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 5005))
s.listen(5)

conn, address = s.accept()
print('Connection address:', address)


def process(key):
    match key:
        case 'w':
            return ('[f' + str(speedVal) + ']') * 4
        case 'a':
            return ('[r' + str(speedVal) + ']') * 2 + ('[f' + str(speedVal) + ']') * 2
        case 's':
            return ('[r' + str(speedVal) + ']') * 4
        case 'd':
            return ('[f' + str(speedVal) + ']') * 2 + ('[r' + str(speedVal) + ']') * 2
        case _:
            return 'Error'


while 1:
    data = conn.recv(20)  # Normally 1024 buffer size, but we want fast response
    if not data:
        break

    packet = data.decode('utf-8')
    conn.send(bytes(packet, encoding='utf-8'))  # echo back input received so client can see what server received

    if packet.isnumeric():
        speedVal = int(packet)*51
        print('Rover speed set to', speedVal)

    if packet.isalpha():
        print(process(packet))

conn.close()
print('Connection Closed.')
