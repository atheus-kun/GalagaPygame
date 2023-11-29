import pygame, random
from shoot_enemie import shoots_enemies
class enemies(pygame.sprite.Sprite):
    def __init__(self,groups,pos,bullets_right,bullets_left,groupBullets):
        super().__init__(groups)
        self.group = groups
        self.groupBullets = groupBullets
        self.animation = 0
        self.trigger_death = 0
        self.state = "idle"
        self.pos = pos
        self.imports()
        self.bullets_right = bullets_right
        self.bullets_left = bullets_left
        self.image = pygame.image.load(self.animations[self.state][self.animation])
        self.rect = self.image.get_rect(center=pos)
        self.salud = 200
        self.lastShoot = 0
        self.cdShoot = 1000
    def health(self):
        if self.state == "idle":
            if pygame.sprite.groupcollide(self.group,self.bullets_left,False,True) and self.salud != 0:
                self.salud -= 50
        if self.state == "idle":
            if pygame.sprite.groupcollide(self.group,self.bullets_right,False,True) and self.salud != 0:
                self.salud -= 50
    def clear(self,dt):
        if self.salud == 0:
            self.state = "boom"
            self.image = pygame.image.load(self.animations[self.state][self.animation])
            if self.current_time >= self.trigger_death +100:
                if self.animation < 5:
                    self.animation += 1
                    self.trigger_death = self.current_time +100*dt
                    self.image = pygame.image.load(self.animations[self.state][self.animation])
        if self.animation == 5 and self.current_time >= self.trigger_death+200:
            pygame.sprite.Sprite.kill(self)
    
    def shoot(self):
        if self.current_time > self.lastShoot + self.cdShoot:
            porcentaje = random.randint(0,10)
            if porcentaje == 5:
                shoots_enemies(self.groupBullets,self.pos)
            self.lastShoot = self.current_time
    def imports(self):
        self.animations = {"idle":["sprites/nave principal/anemies/3.png"],
                           "boom":["sprites/nave principal/animation_boom/boom1.png",
                                   "sprites/nave principal/animation_boom/boom2.png",
                                   "sprites/nave principal/animation_boom/boom3.png",
                                   "sprites/nave principal/animation_boom/boom4.png",
                                   "sprites/nave principal/animation_boom/boom5.png",
                                   "sprites/nave principal/animation_boom/boom6.png"]}
    def update(self,dt):
        self.current_time = pygame.time.get_ticks()
        self.clear(dt)
        self.shoot()
        self.health()