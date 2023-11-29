import pygame
from player import player
from config import *
from shoot import shoots
from enemies import enemies
from collide import collide
class Level:
    def __init__(self):
        #con este llamamos la screen de main
        self.display_surface = pygame.display.get_surface()
        self.player_sprites = pygame.sprite.Group()
        self.bullets_right_sprites = pygame.sprite.Group()
        self.bullets_left_sprites = pygame.sprite.Group()
        self.enemie_sprites = pygame.sprite.Group()
        self.collides = pygame.sprite.Group()
        self.pos_naves = [50,100]
        self.setup()
    def setup(self):
        for i in map_test:
            enemies(self.enemie_sprites,(self.pos_naves[0],self.pos_naves[1]),self.bullets_right_sprites,self.bullets_left_sprites)
            self.pos_naves[0] += 100
            print(self.pos_naves[0])
            print(self.collides,self.enemie_sprites)
        self.player = player((res[0]/2,res[1]/1.2),self.player_sprites,shoots,self.bullets_right_sprites,self.bullets_left_sprites)


    def run(self,dt):
        self.display_surface.fill("black")
        self.bullets_right_sprites.draw(self.display_surface)
        self.bullets_left_sprites.draw(self.display_surface)
        self.player_sprites.draw(self.display_surface)
        self.enemie_sprites.draw(self.display_surface)
        self.collides.draw(self.display_surface)
        self.player_sprites.update(dt)
        self.collides.update(dt)
        self.bullets_right_sprites.update(dt)
        self.bullets_left_sprites.update(dt)
        self.enemie_sprites.update(dt)