import pygame
import sys
import random

pygame.init()

screen_width = 400
screen_height = 400
color = (0, 0, 0)
screen = pygame.display.set_mode((screen_width, screen_height))
screen_rec = screen.get_rect()

star = pygame.image.load("images/star.bmp")
star = pygame.transform.scale(star, (50, 50))
star_rec = star.get_rect()
star_size = 50

laser = pygame.image.load("images/star2.png")
laser = pygame.transform.scale(laser, (50, 50))
laser_rec = laser.get_rect()
laser_size = 50

range_star_x = (0, screen_width - star_size)
range_star_y = (0, screen_height - star_size)
number_of_stars = 5

range_laser_x = (0, screen_width - star_size)
range_laser_y = (0, screen_height - star_size)
number_of_laser = 5


def draw_background():
    pygame.draw.rect(screen, color, pygame.Rect(0, 0, 400, 400))


def draw_stars(i):

    if i < number_of_stars:
        x = random.randrange(*range_star_x)
        y = random.randrange(*range_star_y)
        screen.blit(star, (x, y))
        i += 1
    else:
        print("to many stars")


clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    draw_background()

    draw_stars(0)

    pygame.display.flip()
    clock.tick(1)
