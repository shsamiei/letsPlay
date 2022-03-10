import pygame , consts


class Cells :
    def __init__(self , surface , sx , sy ,color= consts.back_color ):

        self.surface = surface 
        self.sx = sx 
        self.sy = sy 
        self.size = consts.cell_size
        self.color = color
        pygame.draw.rect(surface , (0,0,0) , (self.sx , self.sy , self.size ,self.size) ,1 )
        self.set_color(color)

        
    def set_color(self ,color):
        
        self.color = color 
        pygame.draw.rect(self.surface , color , (self.sx + 1 , self.sy + 1 , self.size - 2 ,self.size -2 ) )
        pygame.display.update()

pass



