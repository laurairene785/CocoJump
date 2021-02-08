import pygame
import sys
from .config import *
from .platform import *
from .player import * 
from .wall import *
import random

class Game :
    def _init_(self):
       pygame.init()
       self.surface = pygame.display.set_mode((width, height))
       pygame.display.set_caption('CocoGame')
       self.running = True
       self.playing = True


    def start(self):
       self.new

    def new (self):       
        self.generate_elements
        self.run


    def run(self):
        while self.running:
            self.events()
            self.draw()
            self.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            self.player.jump()

    def draw (self):
       self.surface.fill(Black)
       self.sprites.draw(self.surface)

    def update (self):
        if self.playing:            
         pygame.display.flip()
         self.sprites.update()
         self.player.validate_platform(self.platform)
         wall = self.player.collide_with(self, walls)
         if wall:
             self.stop()

    def stop(self):
        self.playing = False

    def stop_elements(self, elements):
        for element in elements:
            element.stop()


    
    def generate_elements(self):
        self.platform = Platform()
        self.sprites= pygame.Sprite.Group()        
        self.player = Player(100,self.platform.rect.top-200)
        self.walls= pygame.sprite.Group()
        self.sprites.add(self.platform)
        self.sprites.add(self.player)
        self.wall= Wall(500,self.platform.rect.top)
        self.sprites.add(self.wall)
        

    def generate_walls(self):
        last_position = width +100
        left= random.randrange(last_position + 200, last_position+400)
        if not len(self.walls)>0:
            for w in range(0, C):
                wall = wall(left, self.platform.rect.top)
                last_position = wall.rect.rigth
                self.sprites.add(wall)
                self.walls.add(walls)





