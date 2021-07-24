import pygame,sys
from grid import grid
from agent import agent
from random import choice

class game:
    def __init__(self):
        #General Setup
        pygame.mixer.pre_init(44100,-16,2,512)
        pygame.init()
        self.clock = pygame.time.Clock()

        #Main Window
        self.tile_size = 2
        self.grid_h = 500
        self.grid_w = 500
        self.screen_width = self.tile_size * self.grid_w
        self.screen_height = self.tile_size * self.grid_h
        self.screen = pygame.display.set_mode((self.screen_width,self.screen_height))

        #color
        self.bg_color = (0,0,0)

        #grid
        self.grid = grid(self)
        self.grid.create_grid()
        self.marked_tile_set = set()

        #agent
        self.gen = 0
        self.agent_list = []
        self.agent_group = pygame.sprite.Group()
        self.color_options = lambda: choice([(250,98,63), (34,80,220),(57,230,9)])
        
        a= agent(self,(100,100),self.color_options())
        self.agent_list.append(a)
        self.agent_group.add(a)

        b= agent(self,(400,100),self.color_options())
        self.agent_list.append(b)
        self.agent_group.add(b)

        c= agent(self,(400,400),self.color_options())
        self.agent_list.append(c)
        self.agent_group.add(c)

        d= agent(self,(100,400),self.color_options())
        self.agent_list.append(d)
        self.agent_group.add(d)

    def main_game(self):

        self.agent_group.update()
        self.gen += 1

        #input
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.screen.fill((0,0,0))
                    self.__init__()
                    break
        
        pygame.display.flip()
        pygame.display.set_caption(f"langton's ant - generation: {self.gen} - ants: {len(self.agent_list)} - tiles covered: {len(self.marked_tile_set)}")

        self.clock.tick(120)