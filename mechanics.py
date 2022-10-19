class Ball:
    def __int__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 10
        self.direction = 1
        self.power = 1


class Brick:
    def __int__(self, x, y):
        self.x = x
        self.y = y
        self.hp = 1


class Racket:
    def __int__(self):
        self.x = 10
        self.y = 10
        self.speed = 10
        self.direction = 1


class Game_plan:
    def __int__(self):
        self.map = [[0] * 200] * 200
        self.init_pos()

    def init_pos(self):
        self.map[100][100] = Brick(100, 100)
