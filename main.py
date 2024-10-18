import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvaders:
    """Main Game Class"""

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))
        pygame.display.set_caption(self.settings.caption)

        self.ship = Ship(self)

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

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _draw_screen(self):
            self.screen.fill(self.settings.background_color)
            self.ship.blitme()

            pygame.display.flip()

    def run_game(self):
        """Start the main loop"""

        while True:
            self._check_events()
            self.ship.update()
            self._draw_screen()
            self.clock.tick(self.settings.frame_rate)

if __name__ == '__main__':
    alien_invaders = AlienInvaders()
    alien_invaders.run_game()
        