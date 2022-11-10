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

laser = pygame.image.load("star2.png")
laser = pygame.transform.scale(laser, (50, 50))
laser_rec = laser.get_rect()
laser_size = 50

range_star_x = (0, screen_width - star_size)
range_star_y = (0, screen_height - star_size)
number_of_stars = 5

range_laser_x = (0, screen_width - star_size)
range_laser_y = (0, screen_height - star_size)
number_of_laser = 5

i = 0
while i < number_of_stars:
    x = random.randrange(*range_star_x)
    y = random.randrange(*range_star_y)

    c = random.randrange(*range_laser_x)
    v = random.randrange(*range_laser_y)

    screen.blit(star, (x, y))
    screen.blit(laser, (c, v))


    i += 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()
