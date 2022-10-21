import pygame
import const
from mechanics import Brick, Ball, Racket

class Draw:
    def __int__(self):
        pass

    def draw_map(self,win,map,list_of_blocks):
        self.draw_blocks(win,list_of_blocks)
    def draw_blocks(self,win,list_of_blocks):
        for brick in list_of_blocks:
            self.draw_rect(win,brick)


    def draw_rect(self,win,brick):
        pygame.draw.rect(win, const.RED, pygame.Rect(brick.x * const.SCALE, brick.y * const.SCALE, 1 * const.SCALE , 1 * const.SCALE))
