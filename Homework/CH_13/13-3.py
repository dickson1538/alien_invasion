import pygame, sys
from pygame.sprite import Sprite


class Settings:
    def __init__(self):
        self.screen_width = 600
        self.screen_height = 600
        self.bg_color = (0, 0, 0)
        self.raindrop_speed = .2


class Raindrop(Sprite):
    def __init__(self, rd_game):
        super().__init__()
        self.screen = rd_game.screen
        self.settings = rd_game.settings
        self.image = pygame.image.load('images/rain.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        print(self.rect.width)
        self.y = float(self.rect.y)

    def update(self):
        self.y += self.settings.raindrop_speed
        self.rect.y = self.y


class Raindrops:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        self.raindrops = pygame.sprite.Group()
        self._create_drops()

    def run_game(self):
        while True:
            self.checkevents()
            self.raindrops.update()
            self._update_screen()

    def checkevents(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _create_drops(self):

        drop = Raindrop(self)
        drop_width, drop_height = drop.rect.size
        available_space_x = self.settings.screen_width - drop_width
        number_drops_x = available_space_x // (2 * drop_width)

        available_space_y = self.settings.screen_height
        number_rows = available_space_y // (2 * drop_height)

        for row_number in range(number_rows):
            for drop_number in range(number_drops_x):
                self._create_drop(drop_number, row_number)

    def _create_drop(self, drop_number, row_number):
        drop = Raindrop(self)
        drop_width, drop_height = drop.rect.size
        drop.rect.x = drop_width + 2 * drop_width * drop_number
        drop.y = 2 * drop.rect.height * row_number
        drop.rect.y = drop.y
        self.raindrops.add(drop)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.raindrops.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    rd_game = Raindrops()
    rd_game.run_game()
