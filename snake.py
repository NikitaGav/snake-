snake = [{'x': 2, 'y': 1},
         {'x': 3, 'y': 1},
         {'x': 4, 'y': 1}
         ]
direction = 1
#1-up
#2-down
def move():
    global direction
    new_head = snake[-1]
    snake.append({'x': 5, 'y': 1})
    snake.pop(0)
    print(snake)

move()


def draw():
    pass
 while True:
     pass