import pygame

class Ship:
    """The Ship 🚀"""

    def __init__(self, alien_invaders_game):
        self.settings = alien_invaders_game.settings
        self.screen = alien_invaders_game.screen
        self.screen_rect = alien_invaders_game.screen.get_rect()
        self.image = pygame.image.load('ship.png')
        self.scale = self.settings.ship_scale
        original_width, original_height = self.image.get_size()
        new_width = int(original_width * self.scale)
        new_height = int(original_height * self.scale)
        self.image = pygame.transform.scale(self.image, (new_width, new_height))
        self.rect = self.image.get_rect()
        self.rect.midbottom = (self.screen_rect.midbottom[0], self.screen_rect.midbottom[1] - 20)

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)


