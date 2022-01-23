import pynput
import os
import time

def move():
    pass
def draw():
    snake = [{"X": 2, "Y": 1},
             {"X": 3, "Y": 1},
             {"X": 4, "Y": 1},
             {"X": 4, "Y": 2},
             {"X": 4, "Y": 3},
             {"X": 4, "Y": 4}
             ]

    item = snake[0]
    y = 0
    while y < 20:
        result = ""
        x = 0
        while x < 100:
            char = 'o'
            for item in snake:
                if item['X'] == x and item['Y'] == y:
                    char = "g"
            result += char
            x += 1
        print(result)
        y += 1

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
