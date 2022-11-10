import sys
import pygame



class Key:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 400))

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        print(event.key)
        if event.key == pygame.K_RIGHT:
            self.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _update_screen(self):
        self.screen.fill((0, 0, 0))

        pygame.display.flip()


if __name__ == '__main__':
    kg = Key()
    kg.run_game()