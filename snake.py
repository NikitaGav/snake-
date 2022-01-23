import pynput
import os
import time

direction = 2


def press(key):
    global direction
    if key == pynput.keyboard.Key.down:
        direction = 2
    if key == pynput.keyboard.Key.up:
        direction = 1
    if key == pynput.keyboard.Key.left:
        direction = 4
    if key == pynput.keyboard.Key.right:
        direction = 3

def on_release(key):
    pass

pynput.keyboard.Listener(
    on_press = on_press,
    on_release = on_release
    ).start()
    

def draw():
    pass
while True:
    os.system('cls')
    move()
    draw()
    time.sleep(0.3)
