from const import BLACK
from mechanics import Game_plan
from drawing import Draw
import drawing
class Game:
    def __init__(self, win):
        self.board = None
        self.win = win
        self.win.fill(BLACK)
        self.init()

    def init(self):
        self.game_plan = Game_plan()
        self.drawing = Draw()
        self.drawing.draw_map(self.win, self.game_plan.map, self.game_plan.list_of_blocks)
    def update(self):
        self.drawing.draw_map(self.win,self.game_plan,self.game_plan.list_of_blocks)


