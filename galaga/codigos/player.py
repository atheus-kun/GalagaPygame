import pygame
from config import *
from crono import timer
from shoot import shoots

class player(pygame.sprite.Sprite):
    def __init__(self,pos,group,bullet,group_bullets_right,group_bullets_left):
        super().__init__(group)
        self.status = "idle"
        self.imports()
        self.frame_index = 0
        self.image = pygame.image.load(self.animations[self.status][self.frame_index])
        self.rect = self.image.get_rect(center=pos)
        self.direccion = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 300
        self.Group = group
        self.Bullet = bullet
        self.bullets_right_list = group_bullets_right
        self.bullets_left_list = group_bullets_left
        self.last_shoot = 0
        self.cd_shoot = 500
        self.cd_dash = 500
        self.last_dash = 0
        self.dashing = False
    
    def imports(self):
        self.animations = {"left": ["sprites/nave principal/left/0.png"],
                           "right":["sprites/nave principal/right/0.png"],
                           "idle":["sprites/nave principal/idle/0.png"],}
    
    def input(self,bullet):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.direccion.x = 1
            self.status = "right"
            self.image = pygame.image.load(self.animations[self.status][self.frame_index])
        elif keys[pygame.K_a]:
            self.direccion.x = -1
            self.status = "left"
            self.image = pygame.image.load(self.animations[self.status][self.frame_index])
        else:
            self.direccion.x = 0
            self.status = "idle"
            self.image = pygame.image.load(self.animations[self.status][self.frame_index])
        
        if keys[pygame.K_SPACE]:
            if self.curret_time >= self.last_shoot:
                self.bullets_izq = bullet(self.bullets_left_list,self.pos,25)
                self.bullets_dere = bullet(self.bullets_right_list,self.pos,-25)
                self.bullets_left_list.add(self.bullets_izq)
                self.bullets_right_list.add(self.bullets_dere)
                self.last_shoot = self.curret_time +self.cd_shoot
        if keys[pygame.K_LSHIFT]:
            self.dash()

    def dash(self):
        if self.curret_time >= self.last_dash:
            self.pos.x += self.direccion.x+80
            self.last_dash = self.curret_time + self.cd_dash
    
    def move(self,dt):
        if self.direccion.magnitude() > 0:
            self.direccion = self.direccion.normalize()
        self.pos.x += self.direccion.x* self.speed * dt
        self.rect.centerx = self.pos.x
    
    def update(self,dt):
        self.curret_time = pygame.time.get_ticks()
        self.input(shoots)
        self.move(dt)



    