import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 5005))
s.listen(5)

conn, address = s.accept()
print('Connection address:', address)


def process(key):
    speedVal = 1 * 51
    match key:
        case 'w':
            return ("[f" + str(speedVal) + "]") * 4
        case 'a':
            return ("[r" + str(speedVal) + "]") * 2 + ("[f" + str(speedVal) + "]") * 2
        case 's':
            return ("[r" + str(speedVal) + "]") * 4
        case 'd':
            return ("[f" + str(speedVal) + "]") * 2 + ("[r" + str(speedVal) + "]") * 2
        case _:
            return "Error"


while 1:
    data = conn.recv(20)  # Normally 1024 buffer size, but we want fast response
    if not data:
        break
    print('Obtained:', data.decode("utf-8"))
    conn.send(bytes(process(data.decode("utf-8")), encoding="utf-8"))  # echo

conn.close()
