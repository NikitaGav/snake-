import pynput
import os
import time
import random

snake = [{'x': 2, 'y': 1},
         {'x': 3, 'y': 1},
         {'x': 4, 'y': 1},
         {'x': 4, 'y': 2}
         ]

food = {'x': 10, 'y': 5}

is_food_touch_snake = True
def generate_food():
    is_food_touch_snake = True
    while is_food_touch_snake:
        food['x'] = random.randint(0, 29)
        food['y'] = random.randint(0, 15)
        is_food_touch_snake = False
        for item in snake:
            if food['x'] == item['x'] and food['y'] == item['y']:
                is_food_touch_snake = True


direction = 2
#1-up
#2-down
#3- right
#4-left
def move():
    global direction, food
    new_head = snake[-1].copy()
    if direction == 1:
      new_head['y'] -= 1
    if direction == 2:
      new_head['y'] += 1
    if direction == 3:
      new_head['x'] += 1
    if direction == 4:
      new_head['x'] -= 1
    if new_head['x'] < 0 or new_head['x'] > 29 or new_head['y'] < 0 or new_head['y'] > 14:
        exit("Game over")
    for item in snake:
        if new_head['x'] == item['x'] and new_head['y'] == item['y']:
            exit("Game over")

    if new_head['x'] == food['x'] and new_head['y'] == food['y']:
        generate_food()
    else:
        snake.pop(0)
    snake.append(new_head)


move()


def draw():
    pass
 while True:
     pass