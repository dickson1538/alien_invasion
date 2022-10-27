import pygame
import sys


class RocketGame:
    def __init__(self, game):
        pygame.init()

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load("ship_0005.png")
        self.rect = self.image.get_rect()
        self.rocketocket = Rocket(self)

        pygame.display.set_caption("Rocket Game")


        self.rect.center = self.screen_rect.center

        self.rocket_speed = 1.5

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right, self.moving_left = False, False
        self.moving_up, self.moving_down = False, False

    def run_game(self):
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.settings.rocket_speed

        self.rect.x = self.x
        self.rect.y = self.y

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
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        if event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        if event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False




    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()

        pygame.display.flip()

if __name__ == '__main__':
    ai = RocketGame()
    ai.run_game()

