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
 while True:
     pass