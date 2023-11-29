import pygame
from collide import collide as coll
class enemies(pygame.sprite.Sprite):
    def __init__(self,groups,pos,bullets_right,bullets_left):
        super().__init__(groups)
        self.group = groups
        self.animation = 0
        self.trigger = 0
        self.state = "idle"
        self.imports()
        self.bullets_right = bullets_right
        self.bullets_left = bullets_left
        self.image = pygame.image.load(self.animations[self.state][self.animation])
        self.rect = self.image.get_rect(center=pos)
        self.salud = 100
    def health(self):
        if pygame.sprite.groupcollide(self.group,self.bullets_left,False,True):
            self.salud -= 50
        if pygame.sprite.groupcollide(self.group,self.bullets_right,False,True):
            self.salud -= 50
    def destroy(self):
        pass
    def clear(self):
        if self.salud == 0:
            self.state = "boom"
            self.image = pygame.image.load(self.animations[self.state][self.animation])
            if self.current_time >= self.trigger +100:
                if self.animation < 5:
                    self.animation += 1
                    self.trigger = self.current_time +100
                    self.image = pygame.image.load(self.animations[self.state][self.animation])
        if self.animation == 5 and self.current_time >= self.trigger+200:
            pygame.sprite.Sprite.kill(self)
    def imports(self):
        self.animations = {"idle":["sprites/nave principal/anemies/0.png"],
                           "boom":["sprites/nave principal/animation_boom/boom1.png",
                                   "sprites/nave principal/animation_boom/boom2.png",
                                   "sprites/nave principal/animation_boom/boom3.png",
                                   "sprites/nave principal/animation_boom/boom4.png",
                                   "sprites/nave principal/animation_boom/boom5.png",
                                   "sprites/nave principal/animation_boom/boom6.png"]}
    def update(self,dt):
        self.current_time = pygame.time.get_ticks()
        self.clear()
        self.health()