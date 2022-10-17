from const import BLACK

class Game:
    def __init__(self, win):
        self.board = None
        self.win = win
        self.win.fill(BLACK)

