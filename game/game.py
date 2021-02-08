import pygame
import sys
from .config import *
from .platform import Platform 
from .player import Player 
from .wall import Wall

class Game :
    def _init_(self):
       pygame.init()
       self.surface = pygame.display.set_mode((width, height))
       pygame.display.set_caption('CocoGame')
       self.running = True


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
       pygame.display.flip()
       self.sprites.update()
       self.player.validate_platform(self.platform)

    def stop(self):
        pass

    
    def generate_elements(self):
        self.platform = Platform()
        self.sprites= pygame.Sprite.Group()        
        self.player = Player(100,self.platform.rect.top-200)
        self.sprites.add(self.platform)
        self.sprites.add(self.player)
        self.wall= Wall(500,self.platform.rect.top)
        self.sprites.add(self.wall)





