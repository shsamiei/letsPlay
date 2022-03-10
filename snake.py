
import consts

class Snake :

    dx = {'UP': 0, 'DOWN': 0, 'LEFT': -1, 'RIGHT': 1}
    dy = {'UP': -1, 'DOWN': 1, 'LEFT': 0, 'RIGHT': 0}

    def __init__(self, keys, game, pos, color, direction):

         self.keys = keys 
         self.cells = [pos]
         self.game = game
         self.game.add_snake(self)
         self.color = color
         self.direction = direction
         game.get_cell(pos).set_color(color)
         
         

    def get_head(self):
        print('get_head ')
        return self.cells[-1]

    def handle(self, keys):
        print("snake handle func ")
        #print(keys)
        for key in keys : 
              #print(key)
              if key in self.keys:
                  if self.direction == "LEFT" and self.keys.get(key) != "RIGHT" :
                                 self.direction = self.keys.get(key)
                  if self.direction == "RIGHT" and self.keys.get(key) != "LEFT" :
                                 self.direction = self.keys.get(key)
                  if self.direction == "UP" and self.keys.get(key) != "DOWN" :
                                 self.direction = self.keys.get(key)
                  if self.direction == "DOWN" and self.keys.get(key) != "UP" :
                                 self.direction = self.keys.get(key)
                  

    def val(self, x):
        print("val happen")
        if x < 0:
            x += self.game.size

        if x >= self.game.size:
            x -= self.game.size

        return x

    def next_move(self):
        print("next_move() happen ")
        pos = self.get_head()
        nx , ny =  pos[0] , pos[1]
        nx = self.val(nx + Snake.dx[self.direction])
        ny = self.val(ny + Snake.dy[self.direction])
        new_pos = ( nx , ny )
        color_of_next_pos  = self.game.get_cell(new_pos).color
        print("the color of next cell is : " , color_of_next_pos)
        print("the color of back : " , consts.back_color , "the color of fruit : " , consts.fruit_color)
        if color_of_next_pos != consts.back_color and color_of_next_pos != consts.fruit_color :
            print("kill in next move happen ")
            self.game.kill(self)
        else : 
            if color_of_next_pos == consts.fruit_color : 
                # add this cell to my cells and paint it
                print("fruit color in next move")
                self.cells.append(new_pos)
                self.game.get_cell(new_pos).set_color(self.color)
                pass 
            else : 
                # add this cell and paint it but remove the tail cell 
                print("back color in next move")
                self.cells.append(new_pos)
                self.game.get_cell(new_pos).set_color(self.color)
                self.game.get_cell(self.cells[0]).set_color(consts.back_color)
                self.cells.pop(0)
                