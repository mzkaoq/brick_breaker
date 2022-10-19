import pygame
import const
from mechanics import Brick, Ball, Racket

class Draw:
    def __int__(self):
        pass
    def draw_map(self,win,map):
        for x in map:
            for y in x:
                if x[y] == 0:
                    pass
                elif isinstance(x[y], Brick):
                    self.draw_rect(win,x[y])


    def draw_rect(self,win,brick):
        pygame.draw.rect(win, const.RED, pygame.Rect(brick.x * const.SCALE, brick.y * const.SCALE, 1 * const.SCALE , 1 * const.SCALE))
