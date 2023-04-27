import pygame
from pygame.sprite import Sprite 
from random import randint

class Stars(Sprite):
    """A class to represent a single alien in first."""
    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        #Load the alien image and set its rect attribute.
        self.image = pygame.image.load('star.bmp')
        self.rect = self.image.get_rect()
        #Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #Store the alien's exact horizontal position
        self.x = float(self.rect.x)
