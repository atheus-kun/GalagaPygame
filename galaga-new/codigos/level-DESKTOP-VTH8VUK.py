import pygame
from player import player

from config import *

from shoot_player import shoots_players
from enemies import enemies

class Level:

    def __init__(self):
        #con este llamamos la screen de main
        self.display_surface = pygame.display.get_surface()
        self.player_sprites = pygame.sprite.Group()
        self.bullets_right_sprites = pygame.sprite.Group()
        self.bullets_left_sprites = pygame.sprite.Group()
        self.bulletsEnemies = pygame.sprite.Group()
        self.GroupsCollide = pygame.sprite.GroupSingle()
        self.list_enemies = dict()
        self.pos_naves = [50,100]
        self.numero_enemigo = 0
        self.setup()
    
    def enemiCreator(self):
        for i in mapa_enemigos_lvl1:
            if i == "x":
                self.list_enemies[f"enemigo {self.numero_enemigo}"] = pygame.sprite.GroupSingle()
                enemies(self.list_enemies[f"enemigo {self.numero_enemigo}"],(self.pos_naves[0],self.pos_naves[1]),self.bullets_right_sprites,self.bullets_left_sprites,self.bulletsEnemies)
                self.pos_naves[0] += 100
                self.numero_enemigo += 1
            elif i == "0":
                self.pos_naves[0] += 100
            elif i == "|":
                self.pos_naves[1] += 100
                self.pos_naves[0] = 50

    def enemiDrawer(self,dt):
        for i in range(self.numero_enemigo):
            self.list_enemies[f"enemigo {i}"].draw(self.display_surface)
            self.list_enemies[f"enemigo {i}"].update(dt)

    def setup(self):
        self.enemiCreator()
        self.player = player((res[0]/2,600),self.player_sprites,shoots_players,self.bullets_right_sprites,self.bullets_left_sprites,self.bulletsEnemies,self.GroupsCollide)

    def GameManager(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            if self.player.reborn:
                self.player = player((res[0]/2,600),self.player_sprites,shoots_players,self.bullets_right_sprites,self.bullets_left_sprites,self.bulletsEnemies,self.GroupsCollide)

    def run(self,dt):
        self.GameManager()
        #actualizo la pantalla --------------
        self.display_surface.fill("black")
        #actualizo la pantalla --------------

        #actualizo las balas --------------
        self.bulletsEnemies.draw(self.display_surface)
        self.bullets_right_sprites.draw(self.display_surface)
        self.bullets_left_sprites.draw(self.display_surface)
        self.bullets_right_sprites.update(dt)
        self.bullets_left_sprites.update(dt)
        self.bulletsEnemies.update(dt)
        #actualizo las balas --------------

        #actualizo los players --------------
        self.player_sprites.draw(self.display_surface)
        self.player_sprites.update(dt)
        self.enemiDrawer(dt)
        #actualizo los players --------------

        #actualizo los collides --------------
        self.GroupsCollide.draw(self.display_surface)
        #actualizo los collides --------------