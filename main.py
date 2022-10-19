import pygame
from const import FPS_RATE, SIZE_X, SIZE_Y, SCALE
from game import Game

FPS = FPS_RATE
WIN = pygame.display.set_mode((SIZE_X * SCALE,SIZE_Y * SCALE))
pygame.display.set_caption("pingpongn")

game = Game(WIN)

def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        game.init()
        game.update()
        pygame.display.update()
    pygame.quit()



if __name__ == "__main__":
    main()