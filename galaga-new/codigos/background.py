import pygame
class Back_manager(pygame.sprite.Sprite):
    def __init__(self, groups) -> None:
        super().__init__(groups)
        self.image = pygame.image.load("sprites/nave principal/BG/background.png")
        self.rect = self.image.get_rect(topleft=(0,0))
