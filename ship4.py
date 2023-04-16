import pygame

class Ship:
    """A class to manage the ship."""
    def __init__(self,ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('Intern_Ch12/ship.bmp') #Load the ship image
        self.rect = self.image.get_rect() #and get its rect.
        self.rect.midleft = self.screen_rect.midleft #start each new ship at the bottom center of the screen.
        self.y = float(self.rect.y) #store a float for the ship that's not moving.
        self.moving_right = False #Movement flag; start with a ship that's not moving.
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    def update(self):
        """Update the ship's positionbased on the movement flags."""
        #Update the ship's x value, not the rect.
        if self.moving_down and self.rect.bottom < self.settings.screen_height:
            self.y += self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        #Update rect object from self.x.
        self.rect.y = self.y   
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image,self.rect)