import pygame
import sys
import random

pygame.init()

screen_width = 800
screen_height = 800
color = (0, 0, 0)
screen = pygame.display.set_mode((screen_width, screen_height))
screen_rec = screen.get_rect()

star = pygame.image.load("images/star.bmp")
star = pygame.transform.scale(star, (50, 50))
star_rec = star.get_rect()
star_size = 50

range_star_x = (0, screen_width - star_size)
range_star_y = (0, screen_height - star_size)
number_of_stars = 23


def draw_background():
    pygame.draw.rect(screen, color, pygame.Rect(0, 0, 800, 800))


x_values = []
y_values = []
def draw_star():
    for i in range(10):
        if x_values == 10:
            break
        else:
            x = random.randrange(*range_star_x)
            y = random.randrange(*range_star_y)
            x_values.append(x)
            y_values.append(y)

    for i in range(len(x_values)):
        coordinates = (x_values[i], y_values[i])

    screen.blit(star, coordinates)


clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    draw_background()
    draw_star()

    i = 0



    pygame.display.flip()
    clock.tick(3)
