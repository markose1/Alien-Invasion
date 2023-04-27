import pygame
from pygame.sprite import Sprite

class Raindrops(Sprite):
    """A class to represent a single alien in the fleet."""
    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('star.bmp') # Load the alien image and set its rect attribute.
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width # Start each new alien near the top left of the screen.
        self.rect.y = self.rect.height
        self.y = float(self.rect.y) # Store the alien's exact horizontal position.

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """Move the alien right or left."""
        self.y += self.settings.raindrop_speed * self.settings.rain_direction
        self.rect.y = self.y