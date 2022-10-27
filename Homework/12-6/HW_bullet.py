import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game
        self.settings = ai_game.settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        self.rect = pygame.Rect(0, 0, self.bullet_width, self.bullet_height)
        self.rect.midleft = ai_game.ship.rect.midleft

        self.x = float(self.rect.x)

    def update(self):
        self.x -= self.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.bullet_color, self.rect)
