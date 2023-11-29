import pygame
class collide(pygame.sprite.Sprite):
    def __init__(self,groups,pos):
        super().__init__(groups)
        self.image = pygame.image.load("sprites/nave principal/colliders/2.png")
        self.rect = self.image.get_rect(midtop=pos)