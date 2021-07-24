import pygame

class space():
    def __init__(self, x, y, tile_size):
        self.rect = pygame.Rect(x*tile_size,y*tile_size,tile_size,tile_size)
        self.marked_color = None
    
    def update_marked(self,screen):
        pygame.draw.rect(screen, self.marked_color, self, 0)
    
    def update_unmarked(self,screen):
        pygame.draw.rect(screen, (0,0,0), self, 0)

class grid:
    def __init__(self,game):
        self.game = game
        self.tile_list = []
    
    def create_grid(self):
        for i in range(self.game.grid_w):
            line = []
            for j in range(self.game.grid_h):
                r = space(i,j,self.game.tile_size)
                line.append(r)
            self.tile_list.append(line)




