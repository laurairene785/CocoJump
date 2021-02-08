import pygame
from .config import *
class Platform(pygame.sprite.Sprite):
    def _init_(self):
        pygame.sprite.Sprite._init_(self)
        self.image= pygame.Surface((width, 40))
        self.image.fill(Green)
        self.rect= self.image.get_rect()
        self.rect.x=0
        self.rect.y=height-40