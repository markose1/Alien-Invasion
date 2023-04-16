import pygame
from settings import Settings
class Empty:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Empty")
    def run_game(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print(event.key)
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    e = Empty()
    e.run_game()