import pygame
import const
from mechanics import Brick, Ball, Racket

class Draw:
    def __int__(self):
        pass

    def draw_map(self,win,game_plan):
        self.draw_blocks(win,game_plan.list_of_blocks)
        self.draw_balls(win,game_plan.list_of_balls)
    def draw_blocks(self,win,list_of_blocks):
        for brick in list_of_blocks:
            self.draw_rect(win,brick)
    def draw_balls(self,win,list_of_balls):
        for ball in list_of_balls:
            self.draw_circle(win,ball)

    def draw_rect(self,win,brick):
        pygame.draw.rect(win, const.RED, pygame.Rect(brick.x * const.SCALE, brick.y * const.SCALE, 1 * const.SCALE , 1 * const.SCALE))

    def draw_circle(self,win,ball):
        pygame.draw.circle(win, const.GREY, (ball.x * const.SCALE ,ball.y * const.SCALE), const.SCALE)