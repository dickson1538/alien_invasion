import pygame
import sys
from HW_bullet import Bullet


class Gamecharacter:
    def __init__(self):
        # initialize the game and create game resources

        self.screen = pygame.display.set_mode((800, 500))
        self.ship = pygame.image.load('12-6/ship_0007.png')
        self.ship_rotate = pygame.transform.rotate(self.ship, 270)
        self.ship_rect = self.ship.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.ship_rect.midleft = self.screen_rect.midleft

        self.moving_up = False
        self.moving_down = False

        self.bullets = pygame.sprite.Group()

    def update(self):
        if self.moving_up and self.ship_rect.y > 0:
            self.ship_rect.y -= 1
        if self.moving_down and self.ship_rect.bottom <= self.screen_rect.bottom:
            self.ship_rect.y += 1

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.moving_up = True
                if event.key == pygame.K_DOWN:
                    self.moving_down = True
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    self._fire_bullet()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.moving_up = False
                if event.key == pygame.K_DOWN:
                    self.moving_down = False

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def run_game(self):
        while True:
            self.update()
            self.check_events()
            self.bullets.update()
            self.update_screen()

    def update_screen(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.ship_rotate, self.ship_rect)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()

if __name__ == '__main__':
    ai = Gamecharacter()
    ai.run_game()
