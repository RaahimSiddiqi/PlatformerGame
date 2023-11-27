import pygame

class Coin(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.surf = pygame.image.load("assets/Coin.png")
        self.rect = self.surf.get_rect()

        self.rect.topleft = pos

    def update(self, player):
        if self.rect.colliderect(player.rect):
            player.score += 5
            self.kill()