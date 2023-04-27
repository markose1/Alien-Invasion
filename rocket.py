import pygame
from settings import Settings

class Rocketship:
    """A class to manage the ship."""
    def __init__(self,ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('ship.bmp') #Load the ship image
        self.rect = self.image.get_rect() #and get its rect.
        self.rect.center = self.screen_rect.center #start each new ship at the bottom center of the screen.
        self.x = float(self.rect.x) #store a float for the ship that's not moving.
        self.y = float(self.rect.y)
        self.moving_right = False #Movement flag; start with a ship that's not moving.
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    def update(self):
        """Update the ship's positionbased on the movement flags."""
        #Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.settings.screen_height:
            self.y += self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        #Update rect object from self.x.
        self.rect.x = self.x
        self.rect.y = self.y   
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image,self.rect)