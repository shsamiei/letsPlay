import pygame


class Cells :
    def __init__(self , surface , sx , sy , color ):

        self.surface = surface 
        self.sx = sx 
        self.sy = sy 
        self.size = 100
        self.color = color
        pygame.draw.rect(surface , color , (sx , sy , self.size ,self.size) ,1 )
        self.set_color((32,54,100))

        
    # def set_color(self ,color):
        
    #     self.color = color 
    #     self.sx += 100
    #     self.sy += 100
    #     self.size -= 2
    #     pygame.draw.rect(self.surface , color , (self.sx  , self.sy  , self.size -2  ,self.size -2 ) ,1 )
    #     pygame.display.update()

pass



