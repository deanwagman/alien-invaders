import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, alien_invaders):
        super().__init__()
        self.screen = alien_invaders.screen
        self.settings = alien_invaders.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = alien_invaders.ship.rect.midtop

        self.y = float(self.rect.y)
    
    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


