import pygame


class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.screen_rect = ai_game.screen.get_rect()
        self.ship = pygame.image.load("ship_0007.png")
        self.ship_rotate = pygame.transform.rotate(self.ship, 270)
        self.ship_rect = self.ship.get_rect()
        self.ship_rect.midleft = self.screen_rect.midleft

        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up and self.ship_rect.y > 0:
            self.ship_rect.y -= 1
        if self.moving_down and self.ship_rect.bottom <= self.screen_rect.bottom:
            self.ship_rect.y += 1


    def blitme(self):
        self.screen.blit(self.ship_rotate, self.ship_rect)