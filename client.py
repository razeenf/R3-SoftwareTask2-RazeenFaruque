from pynput import keyboard
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 5005))

validKeys = ['w', 'a', 's', 'd']


def on_press(key):
    try:
        keyChar = format(key.char)
        for i in range(4):
            if keyChar == validKeys[i]:
                s.send(bytes(keyChar, encoding="utf-8"))
                data = s.recv(1024)  # 1024 = buffer size
                print("received data:", data.decode("utf-8"))
    except AttributeError:
        print('not a valid input')


with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press)
listener.start()

s.close()
