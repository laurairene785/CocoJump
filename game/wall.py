import pygame
from .config import *

class Wall(pygame.sprite.Sprite):
     def _init_(self,left, bottom):
        pygame.sprite.Sprite._init_(self)
        self.pygame.Surface((40,80))
        self.image.fill(Purple)
        self.rect= self.image.get_rect()
        self.rect.left=left
        self.rect.bottom=bottom
        self.vel_x = speed

     def update(self):
      
         self.rect.left = self.vel_x

     def stop(self):
         self.vel_x = 0
         self.player.stop()