import pygame
from pygame.locals import *
import sys
import time
from random import randint, randrange
from src.Platform import Platform
from src.Player import Player
from src.Coin import Coin
from src.constants import WIDTH, HEIGHT, FPS

# Comment

def check(sprite, group, margin=40):
    for other_sprite in group:
        if sprite != other_sprite:
            distance_y = abs(sprite.rect.centery - other_sprite.rect.centery)
            
            if distance_y < margin:
                return True
    return False
 
def generate_platforms():
    while len(platformGroup) < 6:
        width = randrange(50,100)
        p  = None      
        C = True
         
        while C:
             p = Platform()
             p.rect.center = (randrange(0, WIDTH-width), randrange(-50, 0))
             C = check(p, platformGroup)

        p.generateCoin(coinGroup, spritesGroup)
        platformGroup.add(p)
        spritesGroup.add(p)
 
def game_over():
    for entity in spritesGroup:
        entity.kill()
        time.sleep(1)
        displaysurface.fill((255,0,0)) # Turn screen red
        pygame.display.update()
        time.sleep(1)
        pygame.quit()
        sys.exit()

def destroy_offscreen_entities():
    # Destroy platforms and coins which have gone off-screen
    if Player1.rect.top <= HEIGHT / 3:
        Player1.pos.y += abs(Player1.vel.y)
        for plat in platformGroup:
            plat.rect.y += abs(Player1.vel.y)
            if plat.rect.top >= HEIGHT:
                plat.kill()

        for coin in coinGroup:
            coin.rect.y += abs(Player1.vel.y)
            if coin.rect.top >= HEIGHT:
                coin.kill()

def render_score():   
    score=font.render(str(Player1.score),True,(123,255,0))   
    displaysurface.blit(score, (WIDTH/2, 10))   

def initialize_platforms():
    for x in range(randint(4,5)):
        C = True
        pl = Platform()
        while C:
            pl = Platform()
            C = check(pl, platformGroup)
        pl.generateCoin(coinGroup, spritesGroup)
        platformGroup.add(pl)
        spritesGroup.add(pl)


if __name__ == "__main__":
    pygame.init()

    FramePerSec = pygame.time.Clock()
    displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Platformer Game")
    background = pygame.image.load("assets/background.png")
    font = pygame.font.SysFont("Verdana", 20)

    # START - Initialization code
    spritesGroup = pygame.sprite.Group()
    platformGroup = pygame.sprite.Group()
    coinGroup = pygame.sprite.Group()
        
    PT1 = Platform(450, 80) 
    PT1.rect = PT1.surf.get_rect(center= (WIDTH/2, HEIGHT-10))
    PT1.moving = False
    PT1.point = False 

    Player1 = Player()

    spritesGroup.add(PT1)
    spritesGroup.add(Player1)
    platformGroup.add(PT1)

    initialize_platforms()
    # END - Initialization Code

    while True:
        # Event Loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:    
                if event.key == pygame.K_SPACE:
                    Player1.jump(platformGroup)
            if event.type == pygame.KEYUP:    
                if event.key == pygame.K_SPACE:
                    Player1.cancel_jump()

        # Game over if Player falls below the screen
        if Player1.rect.top > HEIGHT:
            game_over()

        displaysurface.blit(background, (0,0))  # Clear screen
        destroy_offscreen_entities()  # Clear outdated entries    
        generate_platforms()  # Generate new platforms 
        render_score()  # Update and render score
        
        # Update and render all sprites
        for entity in spritesGroup:
            displaysurface.blit(entity.surf, entity.rect)
            if type(entity) == Platform or type(entity) == Coin:
                entity.update(Player1)
            elif type(entity) == Player:
                entity.update(platformGroup)
            else:
                entity.update()
    
        pygame.display.update()
        FramePerSec.tick(FPS)
