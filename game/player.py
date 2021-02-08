import pygame
from .config import * 
from platform import *


class Player(pygame.sprite.Sprite):
    def _init_(self,left, bottom):
        pygame.sprite.Sprite._init_(self)
        self.pos_y = self.rect.bottom
        self.vel_y=0
        self.can_jump= False
        self.image= pygame.Surface((40,40))
        self.image.fill(Blue)
        self.rect= self.image.get_rect()
        self.rect.left=left
        self.rect.bottom= bottom
    

    def validate_platform(self, platform):
        result= pygame.sprite.collide_rect(self,platform)
        if result:
            self.vel_y = 0
            self.pos_y = platform.rect.top
        
    def update_pos(self):
        self.vel_y += 1.2
        self.pos_y+= self.vel_y+0.5*1.2
    
    def update(self):
        self.update_pos()
        self.rect.bottom = self.self.pos_y

    def jump(self):
        if self.can_jump:
             self.vel_y=-23
             self.can_jump= False



    
