import pygame


class Cells :
    def __init__(self , surface , sx , sy , color ):

        self.surface = surface 
        self.sx = sx 
        self.sy = sy 
        self.size = 30
        self.color = color
        pygame.draw.rect(surface , (0,0,0) , (self.sx , self.sy , self.size ,self.size) ,1 )
        self.set_color(color)

        
    def set_color(self ,color):
        
        self.color = color 
        pygame.draw.rect(self.surface , color , (self.sx + 1 , self.sy + 1 , self.size - 2 ,self.size -2 ) )
        pygame.display.update()

pass



