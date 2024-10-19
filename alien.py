import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """👾"""

    def __init__(self, alien_invaders):
        super().__init__()

        self.screen = alien_invaders.screen
        self.settings = alien_invaders.settings
        self.screen_rect = self.screen.get_rect()

        # Image and Rect w/ scaling
        self.image = pygame.image.load("alien.png")
        original_width, original_height = self.image.get_size()
        new_width = original_width * self.settings.alien_scale
        new_height = original_height * self.settings.alien_scale
        self.image = pygame.transform.scale(self.image, (new_width, new_height))
        self.rect = self.image.get_rect()

        self.rect.x = new_width
        self.rect.y = new_height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        self.screen.blit(self.image, self.rect)


