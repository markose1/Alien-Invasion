import pygame

class WolvesLogo:
    """A class to manage the ship."""
    def __init__(self,twolves):
        """Initialize the ship and set its starting position."""
        self.screen = twolves.screen
        self.screen_rect = twolves.screen.get_rect()
        self.image = pygame.image.load('Intern_Ch12/twolves.bmp') #Load the Twolves logo
        self.rect = self.image.get_rect() #and get its rect.
        self.rect.center = self.screen_rect.center #start each new ship at the center of the screen.
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image,self.rect)