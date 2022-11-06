import pygame
import sys
import random

pygame.init()

screen_width = 400
screen_height = 400

screen = pygame.display.set_mode((400, 400))
screen_rec = screen.get_rect()

star = pygame.image.load("star.bmp")
star = pygame.transform.scale(star, (50, 50))
star_rec = star.get_rect()
star_size = 50

range_x = (0, screen_width - star_size)
range_y = (0, screen_height - star_size)
number_of_stars = 10

i = 0
while i < number_of_stars:
    x = random.randrange(*range_x)
    y = random.randrange(*range_y)
    screen.blit(star, (x, y))
    i += 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()
