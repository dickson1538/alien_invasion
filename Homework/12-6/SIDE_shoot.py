import pygame
import sys
from SHIP import Ship
from Side_settings import Settings


class AlienInvasion:

    def __init__(self):
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()

        self.screen = pygame.display.set_mode((800, 800))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.ship.moving_up = True
                if event.key == pygame.K_DOWN:
                    self.ship.moving_down = True


            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.ship.moving_up = False
                if event.key == pygame.K_DOWN:
                    self.ship.moving_down = False


    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()



        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
