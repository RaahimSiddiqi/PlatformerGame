import pygame
from pygame.locals import *
from .constants import FRIC, WIDTH, ACC

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.surf = pygame.image.load("assets/snowman_R.png")
        self.rect = self.surf.get_rect()
   
        self.pos = pygame.math.Vector2((10, 360))
        self.vel = pygame.math.Vector2(0,0)
        self.acc = pygame.math.Vector2(0,0)
        self.jumping = False
        self.score = 0 

    def change_acceleration(self, keys):
        if keys[K_LEFT]:
            self.surf = pygame.image.load("assets/snowman_L.png")
            self.acc.x = -ACC
        if keys[K_RIGHT]:
            self.surf = pygame.image.load("assets/snowman_R.png")
            self.acc.x = ACC
 
    def move(self):
        self.acc = pygame.math.Vector2(0,0.5)
        self.change_acceleration(pygame.key.get_pressed())
                
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.update_position()
        
    def update_position(self):
        if self.pos.x > WIDTH + 20:
            self.pos.x = 0
        if self.pos.x < -20:
            self.pos.x = WIDTH
             
        self.rect.midbottom = self.pos
 
    def jump(self, platformGroup): 
        hits = pygame.sprite.spritecollide(self, platformGroup, False)
        if hits and not self.jumping:
           self.jumping = True
           self.vel.y = -15
           return True
        return False
 
    def cancel_jump(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3
 
    def update(self, platformGroup):
        self.move()
        
        hits = pygame.sprite.spritecollide(self, platformGroup, False)
        if self.vel.y > 0:        
            if hits:
                if self.pos.y < hits[0].rect.bottom:
                    if hits[0].point == True:   
                        hits[0].point = False   
                        self.score += 1          
                    self.pos.y = hits[0].rect.top +1
                    self.vel.y = 0
                    self.jumping = False