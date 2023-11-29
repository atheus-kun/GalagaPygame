import pygame
from config import *
class shoots_players(pygame.sprite.Sprite):
    def __init__(self,Group,pos,lado):
        super().__init__(Group)
        self.group = Group
        self.image = pygame.image.load("sprites/nave principal/shoots/disparo_2_new.png")
        self.rect = self.image.get_rect(midtop=(pos.x-lado,pos.y))
        self.direccion = -1
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 400
    def shooted(self,dt):
        self.pos.y += self.direccion* self.speed * dt
        self.rect.centery = self.pos.y
    def clear(self):
        if self.pos.y < -1:
            pygame.sprite.Sprite.kill(self)
    def update(self,dt):
        self.clear()
        self.shooted(dt)

