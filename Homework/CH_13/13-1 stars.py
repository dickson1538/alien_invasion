import pygame
import sys

pygame.init()

TILE_SIZE = 50

screen = pygame.display.set_mode((10*TILE_SIZE, 10*TILE_SIZE))
screen_rec = screen.get_rect()
star = pygame.image.load("star.bmp")
star = pygame.transform.scale(star, (50, 50))

star_rec = star.get_rect()
print(star_rec)
num_titles = screen_rec.width // star_rec.width

for y in range(num_titles):
    for x in range(num_titles):
        screen.blit(star, (x * star_rec.width, y * star_rec.height))


while True:
    # 1 check for user input (key press, mouse clicks,joystick)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("thanks for playing")
            sys.exit()
        # change the background if a key is
        # pressed or released
        if event.type == pygame.KEYUP:
            screen.fill((0, 0, 255))
        if event.type == pygame.KEYDOWN:
            screen.fill((255, 255, 0))



    pygame.display.flip()