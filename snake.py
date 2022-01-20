snake = [{'x': 2, 'y': 1},
         {'x': 3, 'y': 1},
         {'x': 4, 'y': 1}
         ]
direction = 2
#1-up
#2-down
def move():
    global direction
    new_head = snake[-1].copy()
    if direction == 1:
      new_head['y'] -= 1
    if direction == 2:
      new_head['y'] += 1
    snake.append(new_head)
    snake.pop(0)
    print(snake)

move()


def draw():
    pass
 while True:
     pass