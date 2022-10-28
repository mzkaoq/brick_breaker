class Ball:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.speed = 10
        self.direction_x = 1
        self.direction_y = 1
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
        self.init_pos()

    def init_pos(self):
        self.add_block(100,100)

    def add_block(self,x,y):
        new_block = Brick(x, y)
        self.map[x][y]= new_block
        self.list_of_blocks.append(new_block)

    def remove_block(self,x,y):
        self.map[x][y] = 0
        for block in self.list_of_blocks:
            if block.x == x and block.y == y:
                self.list_of_blocks.remove(block)

