import random
from const import  SIZE_X, SIZE_Y, SCALE
class Ball:
    def __init__(self):
        self.x = 100
        self.y = 180
        self.speed = 3
        self.direction_x = round(random.uniform(-1,1),2)
        self.direction_y = -1
        self.power = 1

    def change_speed(self,amount):
        self.speed *= amount


class Brick:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.hp = 1


class Racket:
    def __init__(self):
        self.x = 10
        self.y = 10
        self.speed = 10
        self.direction = 1


class Game_plan:
    def __init__(self):
        self.map = [[0 for x in range(200)] for y in range(200)]
        self.list_of_blocks = []
        self.list_of_balls = []
        self.init_pos()

    def init_pos(self):
        for x in range(50,150):
            for y in range(40,60):
                self.add_block(x,y)
        self.add_ball()

    def add_block(self,x,y):
        new_block = Brick(x, y)
        self.map[x][y]= new_block
        self.list_of_blocks.append(new_block)

    def remove_block(self,x,y):
        self.map[x][y] = 0
        for block in self.list_of_blocks:
            if block.x == x and block.y == y:
                self.list_of_blocks.remove(block)

    def add_ball(self):
        new_ball = Ball()
        self.list_of_balls.append(new_ball)

    def remove_ball(self,ball):
        self.list_of_balls.remove(ball)

    def update_balls(self):
        for ball in self.list_of_balls:
            ball.x += ball.speed * ball.direction_x
            ball.y += ball.speed * ball.direction_y
            if ball.x >= SIZE_X or ball.x <= 0:
                ball.direction_x *= -1
            if ball.y >= SIZE_Y or ball.y <= 0:
                ball.direction_y *= -1
