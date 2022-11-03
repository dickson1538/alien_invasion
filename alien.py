import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, ai_game):
        super().__init__()     # init the sprite libary
        self.screen = ai_game.screen
        self.settings = ai_game.settings   # to get the speed of the alien

        # loading the alien image and its rect
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # alien starts top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # store alien horizontal postion
        self.x = float(self.rect.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)    # this is the fleet direction 1,-1 changes it
        self.rect.x = self.x
