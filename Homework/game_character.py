import time
import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))
screen.fill((0, 0, 240))


ship=pygame.image.load('ship_0005.png')
ship_rect = ship.get_rect()
screen_rect = screen.get_rect()

ship_rect.center = screen_rect.center

screen.blit(ship, ship_rect)


pygame.display.flip()
time.sleep(9)

