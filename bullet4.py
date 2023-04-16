#Creating the Bullet Class
import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""
    def __init__(self,ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,self.settings.bullet_height) 
        """Create a bullet rect at (0,0) and then set correct position."""
        self.rect.midright = ai_game.ship.rect.midright
        self.x = float(self.rect.x)
        """Store the bullet's position as a float."""
    def update(self):
        """Move the bullet up the screen."""
        self.x += self.settings.bullet_speed #Update the exact position of the bullet.
        self.rect.x = self.x #Update the rect position
    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen,self.color,self.rect)