import pygame
from cells import Cells
# we should start pygame and its stuff :

pygame.init()
screen = pygame.display.set_mode((800 , 600))
screen.fill((255,255,120))

newOne = Cells(screen , 10 , 10 , (0,0,0))
#i = 10 
while True :
    screen.fill((255,255,120))
    newOne = Cells(screen , 10, 10 , (0,0,0))
    # i += 1
    pygame.display.update()
    pygame.time.delay(13)
    pygame.event.pump()
