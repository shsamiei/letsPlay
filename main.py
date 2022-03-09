import pygame , consts ,sys
from cells import Cells
from gameManager import GameManager

# we should start pygame and its stuff :

pygame.init()
screen = pygame.display.set_mode((700 , 700))
screen.fill((255,255,255))
game = GameManager(20 , screen , 30 ,50 ,consts.block_cells)




while True:
        events = pygame.event.get()
        keys = []
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                keys.append(event.unicode)
        #game.handle(keys)
        pygame.time.wait(100)