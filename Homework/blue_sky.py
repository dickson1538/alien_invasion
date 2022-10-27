import pygame

while True:
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    screen.fill((0, 0, 240))
    pygame.display.flip()


# or no loop and use a .timesleep


def __init__(self):
    self.image = pygame.image.load('ship_0005.png')
    self.rect - self.image.get_rect()
    self.rect.midbottom = self.screen_rect.midbottom
    self.ship = Ship(self)


def blitme(self):
    self.screen.blit(self.image, self.rect)
