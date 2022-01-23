import pynput
import os
import time

def move():
    pass
def draw():
    snake = [{"snakeX": 2, "snakeY": 1},
             {"snakeX": 3, "snakeY": 1},
             {"snakeX": 4, "snakeY": 1},
             {"snakeX": 4, "snakeY": 2},
             {"snakeX": 4, "snakeY": 3},
             {"snakeX": 4, "snakeY": 4}
             ]

    item = snake[0]
    y = 0
    while y < 20:
        result = ""
        x = 0
        while x < 100:
            char = 'o'
            for item in snake:
                if item['snakeX'] == x and item['snakeY'] == y:
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
