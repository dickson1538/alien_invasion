import pygame
import sys

pygame.init()

TILE_SIZE = 50

screen = pygame.display.set_mode((10*TILE_SIZE, 10*TILE_SIZE))
screen_rec = screen.get_rect()
star = pygame.image.load("images/star.bmp")
star = pygame.transform.scale(star, (50, 50))

star_rec = star.get_rect()
num_titles = screen_rec.width // star_rec.width

for y in range(num_titles):
    for x in range(num_titles):
        screen.blit(star, (x * star_rec.width, y * star_rec.height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.flip()