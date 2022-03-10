import pygame , consts
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
                t = Cells(screen, self.sx + i * 30, self.sy + j * 30 )
                tmp.append(t)
            self.cells.append(tmp)

        for cell in block_cells:
            self.get_cell(cell).set_color(consts.block_color)

        pass

    def add_snake(self, snake):
        self.snakes.append(snake)

    def kill(self, killed_snake):
        self.snakes.remove(killed_snake)


    def get_cell(self, pos):
        try:
            return self.cells[pos[0]][pos[1]]
        except:
            return None

    def get_next_fruit_pos(self): # returns tuple (x, y) that is the fruit location
        ret = -1, -1
        mx = -100

        for i in range(0, self.size):
            for j in range(0, self.size):

                mn = 100000000

                for x in range(0, self.size):
                    for y in range(0, self.size):
                        if self.get_cell((x, y)).color != consts.back_color:
                            mn = min(mn, int( abs(x-i) + abs(y-j) ))


                if mn > mx:
                    mx = mn
                    ret = i, j

        return ret

    def handle(self, keys):
        self.snakes[0].next_move()
        pass