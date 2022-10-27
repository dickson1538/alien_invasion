import time
import pygame
import sys


class Gamecharacter:
    def __init__(self):
        # initialize the game and create game resources

        self.screen = pygame.display.set_mode((800, 500))
        self.ship = pygame.image.load('12-6/ship_0007.png')
        self.ship_rect = self.ship.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.ship_rect.center = self.screen_rect.center

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.ship_rect.right < self.screen_rect.right:
            self.ship_rect.x += 1
        if self.moving_left and self.ship_rect.left > 0:
            self.ship_rect.x -= 1
        if self.moving_up and self.ship_rect.y > 0:
            self.ship_rect.y -= 1
        if self.moving_down and self.ship_rect.bottom <= self.screen_rect.bottom:
            self.ship_rect.y += 1

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.moving_right = True
                if event.key == pygame.K_LEFT:
                    self.moving_left = True
                if event.key == pygame.K_UP:
                    self.moving_up = True
                if event.key == pygame.K_DOWN:
                    self.moving_down = True


            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.moving_left = False
                if event.key == pygame.K_UP:
                    self.moving_up = False
                if event.key == pygame.K_DOWN:
                    self.moving_down = False
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

    def run_game(self):
        while True:
            self.check_events()
            self.update()
            self.update_screen()

    def update_screen(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.ship, self.ship_rect)
        pygame.display.flip()


if __name__ == '__main__':
    ai = Gamecharacter()
    ai.run_game()
