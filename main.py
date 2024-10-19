import sys
import pygame

from settings import Settings

from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvaders:
    """Main Game Class"""

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))
        pygame.display.set_caption(self.settings.caption)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_alien_fleet()

    def _fire_bullet(self):
        """Pew Pew"""
        if len(self.bullets) < self.settings.maximum_number_of_bullets:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)

    def _draw_bullets(self):
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

    def _create_alien_fleet(self):
        alien = Alien(self)
        alien_width = alien.rect.width
        current_x = alien.rect.x
        spacing = self.settings.alien_spacing


        while current_x + alien.rect.width + spacing < self.settings.width:
            new_alien = Alien(self)
            new_alien.x = current_x
            new_alien.rect.x = current_x
            self.aliens.add(new_alien)
            current_x = current_x + alien_width + spacing

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _draw_screen(self):
            self.screen.fill(self.settings.background_color)
            self.ship.blitme()
            self._draw_bullets()
            self.aliens.draw(self.screen)

            pygame.display.flip()

    def run_game(self):
        """Start the main loop"""

        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._draw_screen()
            self.clock.tick(self.settings.frame_rate)

if __name__ == '__main__':
    alien_invaders = AlienInvaders()
    alien_invaders.run_game()
        