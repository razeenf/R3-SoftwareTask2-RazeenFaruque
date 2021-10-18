# Rover Navigation Controls

For this task I built simple navigation controls to control a rover with a 
keyboard, this was done by utilizing the Pynput library. First I ask the client
user to enter an initial speed for the rover then the client can use the WASD
keys to move the rover forward, back, left and right. If the user wants to
change the speed of the Rover they can simply press a number from 0-5 at anytime
and the speed will automatically be changed. The esc key is used to disconnect 
from the server and end the program. Any keys other than WASD, 0-5 
and esc will be ignored and have no effect on the program. 

https://user-images.githubusercontent.com/91243266/137671059-dea5fa3b-8b8f-4829-bc23-1fc9d6c5d186.mp4

The way this works is that  input.py (client) uses pynput to track 
which key the user presses and if a valid key is pressed then that key char
is sent to the output.py (server), the server then echos back the received 
data to the client and then checks to see whether a letter or number was received. 

- If a letter is received then the process function 
is called, this function just contains a simple switch statement that prints 
the respective output based on which letter key was received. 

- If a number is received it is converted to an integer and set to the
speedVal variable which changes the rovers speed.

An AttributeError try catch is in place in case a non char key is pressed,
in such case nothing happens unless it was the esc key that was pressed. 
If esc is pressed the client and server will be disconnected, the pynput keyboard listener 
will stop and the program will end. 
