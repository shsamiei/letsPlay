import pygame
from cells import Cells

class GameManager :

    def __init__(self , size , screen , sx , sy , block_cells):

        self.screen = screen
        self.size = size
        self.cells = []
        self.sx = sx 
        self.sy = sy
        self.snakes = []
        #self.turn = 0 
        for i in range(self.size):
            tmp = []
            for j in range(self.size):
                t = Cells(screen, self.sx + i * 30, self.sy + j * 30 ,(255, 255, 255))
                tmp.append(t)
            self.cells.append(tmp)

        for cell in block_cells:
            self.get_cell(cell).set_color((0, 137, 168))

        pass

    def get_cell(self, pos):
        try:
            return self.cells[pos[0]][pos[1]]
        except:
            return None