from pynput import keyboard
import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
time.sleep(3)   # used to delay connection so client doesn't crash right away
s.connect(('127.0.0.1', 5005))
validKeys = ['w', 'a', 's', 'd', '0', '1', '2', '3', '4', '5']

while 1:        # Validation check to make sure first input is a number
    speedVal = input('enter rover speed (0-5): ')
    if speedVal.isnumeric() and 0 <= int(speedVal) <= 5:
        s.send(bytes(format(speedVal), encoding='utf-8'))
        print('echo:', s.recv(1024).decode('utf-8'))
        break


def on_press(key):
    try:
        for i in range(10):
            if key.char == validKeys[i]:    # checks to see if key pressed is apart of valid keys
                s.send(bytes(format(key.char), encoding='utf-8'))   # if so sends key value to server
                print('echo:', s.recv(1024).decode('utf-8'))    # prints what key value server received
    except AttributeError:  # catches special keys pressed
        if key == keyboard.Key.esc:  # if esc program ends otherwise nothing
            print('Connection Closed.')
            s.close()
            listener.stop()


with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()

