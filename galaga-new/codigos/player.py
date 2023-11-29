import pygame
from config import *
from shoot_player import shoots_players

class player(pygame.sprite.Sprite):
    def __init__(self,pos,group,bullet,group_bullets_right,group_bullets_left,group_bullet_enemies):
        super().__init__(group)
        #variables---------------------
        self.Group = group
        self.Bullet = bullet
        self.bullets_right_list = group_bullets_right
        self.bullets_left_list = group_bullets_left
        self.bullets_enemies_list = group_bullet_enemies
        #variables---------------------

        #sprite---------------------
        self.imports()
        self.animation = 0
        self.status = "idle"
        self.image = pygame.image.load(self.animations[self.status][self.animation])
        self.rect = self.image.get_rect(center=pos)
        self.direccion = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        #sprite---------------------

        #velocidad y salud-------------------
        self.trigger_death = 0
        self.speed = 300
        self.salud = 200
        #velocidad y salud-------------------

        #disparo-------------------
        self.last_shoot = 0
        self.cd_shoot = 500
        #disparo-------------------

        #dash----------------------
        self.cd_dash = 500
        self.last_dash = 0
        self.dashing = False
        #dash----------------------

        #invulnerabilidad----------------------
        self.cd_strike = 500
        self.last_strike = 0
        self.Strike = False
        #invulnerabilidad----------------------

    def move(self,dt):
        if self.direccion.magnitude() > 0:
            self.direccion = self.direccion.normalize()
        self.pos.x += self.direccion.x* self.speed * dt
        self.rect.centerx = self.pos.x
    
    def imports(self):
        self.animations = {"left": ["sprites/nave principal/left/0.png"],
                           "right":["sprites/nave principal/right/0.png"],
                           "idle":["sprites/nave principal/idle/0.png"],
                           "boom":["sprites/nave principal/animation_boom/boom1.png",
                                   "sprites/nave principal/animation_boom/boom2.png",
                                   "sprites/nave principal/animation_boom/boom3.png",
                                   "sprites/nave principal/animation_boom/boom4.png",
                                   "sprites/nave principal/animation_boom/boom5.png",
                                   "sprites/nave principal/animation_boom/boom6.png"]}
    
    def health(self,dt):
        if self.salud == 0:
            self.status = "boom"
            self.image = pygame.image.load(self.animations[self.status][self.animation])
            if self.current_time >= self.trigger_death +100:
                if self.animation < 5:
                    self.animation += 1
                    self.trigger_death = self.current_time +100*dt
                    self.image = pygame.image.load(self.animations[self.status][self.animation])
        if self.animation == 5 and self.current_time >= self.trigger_death+200:
            pygame.sprite.Sprite.kill(self)
        if pygame.sprite.groupcollide(self.Group,self.bullets_enemies_list,False,True)  and self.salud != 0:
            self.salud -= 50
    
    def input(self,bullet):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and not self.salud == 0:
            self.direccion.x = 1
            self.status = "right"
            self.image = pygame.image.load(self.animations[self.status][self.animation])
        elif keys[pygame.K_a] and not self.salud == 0:
            self.direccion.x = -1
            self.status = "left"
            self.image = pygame.image.load(self.animations[self.status][self.animation])
        else:
            self.direccion.x = 0
            if not self.salud == 0:
                self.status = "idle"
                self.image = pygame.image.load(self.animations[self.status][self.animation])
        
        if keys[pygame.K_SPACE]:
            if self.current_time >= self.last_shoot:
                self.bullets_izq = bullet(self.bullets_left_list,self.pos,20)
                self.bullets_dere = bullet(self.bullets_right_list,self.pos,-20)
                self.bullets_left_list.add(self.bullets_izq)
                self.bullets_right_list.add(self.bullets_dere)
                self.last_shoot = self.current_time +self.cd_shoot
        if keys[pygame.K_LSHIFT]:
            self.dash()

    def dash(self):
        pass
    
    def update(self,dt):
        self.current_time = pygame.time.get_ticks()
        self.health(dt)
        self.input(shoots_players)
        self.move(dt)



    