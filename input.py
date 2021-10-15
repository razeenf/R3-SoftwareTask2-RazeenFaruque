from pynput import keyboard
import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
time.sleep(1)
s.connect(('127.0.0.1', 5005))

validKeys = ['w', 'a', 's', 'd']

while 1:
    speedVal = input('enter rover speed (0-5): ')
    if speedVal.isnumeric() and 0 <= int(speedVal) <= 5:
        s.send(bytes(format(speedVal), encoding='utf-8'))
        print('echo:', s.recv(1024).decode('utf-8'))
        break


def on_press(key):
    try:
        for i in range(4):
            if format(key.char) == validKeys[i]:
                s.send(bytes(format(key.char), encoding='utf-8'))
                data = s.recv(1024)  # 1024 = buffer size
                print('echo:', data.decode('utf-8'))
    except AttributeError:
        if key == keyboard.Key.esc:
            print('Connection Closed.')
            s.close()
            listener.stop()


with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()

listener = keyboard.Listener(
    on_press=on_press)
listener.start()
