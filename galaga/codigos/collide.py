import pygame
class collide(pygame.sprite.Sprite):
    def __init__(self,groups,pos) -> None:
        super().__init__(groups)
        self.image = pygame.image.load("sprites/nave principal/colliders/0.png")
        self.rect = self.image.get_rect(center=pos)