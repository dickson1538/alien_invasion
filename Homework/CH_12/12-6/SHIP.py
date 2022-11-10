import pygame


class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect

        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load("ship_0007.png")
        self.image_rotate = pygame.transform.rotate(self.image, 270)
        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft

        self.y = float(self.rect.y)

        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up and self.rect.y > 0:
            self.rect.y -= 1
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.rect.y += 1


    def blitme(self):
        self.screen.blit(self.image_rotate, self.rect)