import pygame, math, random

class agent(pygame.sprite.Sprite):
    def __init__(self,game,grid_pos,trace_color):
        super().__init__()
        self.game = game

        self.image = pygame.Surface((self.game.tile_size // 2, self.game.tile_size // 2))
        self.rect = self.image.get_rect()

        self.grid_pos = grid_pos
        self.dir = 0
        self.x, self.y = self.grid_pos
        self.current_tile = self.game.grid.tile_list[self.x][self.y]
        
        self.trace_color = trace_color
    
    def update(self):

        self.current_tile = self.game.grid.tile_list[self.x][self.y]
        self.current_tile.marked_color = self.trace_color

        self.x, self.y = self.grid_pos    

        #rules / direction
        if self.current_tile in self.game.marked_tile_set :
            self.dir += 1 #derecha
            self.dir = self.dir%4
            self.game.marked_tile_set.remove(self.current_tile)
            self.current_tile.update_unmarked(self.game.screen)
        else:
            self.dir -= 1 #izquierda
            self.dir = self.dir%4
            self.game.marked_tile_set.add(self.current_tile) 
            self.current_tile.update_marked(self.game.screen)           

        #movement
        if self.dir == 0:
            self.y -= 1
        elif self.dir == 1:
            self.x += 1
        elif self.dir == 2:
            self.y += 1
        elif self.dir == 3:
            self.x -= 1
        
        #constrain
        if self.x > self.game.grid_w-1 : self.x -=(self.game.grid_w-1)
        if self.x < 0 : self.x +=(self.game.grid_h)
        if self.y > self.game.grid_h-1 : self.y -=(self.game.grid_h-1)
        if self.y < 0 : self.y +=(self.game.grid_w)

        self.grid_pos = (self.x,self.y)
        self.rect.center = self.current_tile.rect.center

