import pygame
import time

pygame.init()
screen = pygame.display.set_mode((400, 400))
screen.fill((0, 0, 240))
pygame.display.flip()
time.sleep(3)

# or no loop and use a .timesleep
