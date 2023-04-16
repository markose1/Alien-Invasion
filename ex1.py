"""Make background Blue,find bitmap image create a class for 
it and match the color of the image to background."""
import sys
import pygame
from settings2 import Settings
from logo import WolvesLogo
class Twolves:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Timberwolves")
        self.logo = WolvesLogo(self)
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)
    def _check_events(self):    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        #Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.logo.blitme()
        #Make the most recently drawn screen visible6
        pygame.display.flip()
if __name__ == '__main__':
    #Make a instance, and run the game.
    wolves = Twolves()
    wolves.run_game()