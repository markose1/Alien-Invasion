import sys
import pygame
from settings5 import Settings
from ship import Ship
from bullet import Bullet
from star import Stars

class Star:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init() #initializes the background settings that Pygame needs to work properly
        self.clock = pygame.time.Clock() #we create an instance of the class 'Clock'
        self.settings = Settings()
        #self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) #tells Pygame to figure out a window size that will fill the screen
        """creates a display window that we'll draw all the game's graphical elements. 
        The argument (0,0) is a tuple that defines the dimensions of the game window,
        and because we don't know the width ad height of the screen, we have the 'FULLSCREEN' 
        parameter it tells python to figure out a window size that fits the screen."""
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) #we update the height and width after the screen is created
        pygame.display.set_caption("Star Invasion") 
        self.ship = Ship(self) #import Ship class and make an instance of Ship
        self.bullets = pygame.sprite.Group() #Storing Bullets in a Group
        self.stars = pygame.sprite.Group()
        self._create_fleet()
        
    def run_game(self): #Controls the game
        """Start the main loop for the game."""
        while True: 
            """Watch for keyboard and mouse events."""
            self._check_events()
            self.ship.update()
            """Get rid of bullets that have disappeared."""
            self._update_bullets()
            self._update_screen()
            """Makes the most recently drawn screen visible. Continually updates the display to show 
            the new positions of game elements and hide the old ones, creating the illusion of smooth movement."""
            self.clock.tick(60) #sets the frame rate in the argument, makes the loop run 60 times per second
    
    def _check_events(self):
        """Respond to key presses and mouse events."""
        for event in pygame.event.get(): #Event loop manages the screen updates,listens for events and perform appropriate tasks depending on the kind of event that occurs.
            """To access the events that Pygame detects, we use the function 'pygame.event.get()'. Which returns a list of events 
            that have taken place since the last time we called the function. Any keyboard or mouse event will cause this for loop to run"""
            if event.type == pygame.QUIT: #when the player clicks the game window"s close button, a pygame.QUIT event is detected
                """meant to detect and respond to specific events.""" 
                sys.exit() #calls sys.exit() to exit the game.
            elif event.type == pygame.KEYDOWN: #responds to keydown event
                self._check_keydown_events(event) #checks to see if the right arrow key was pressed
            elif event.type == pygame.KEYUP: #responds to keyup event
                self._check_keyup_events(event) #checks to see if the player released the right arrow key 
    
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT: #checks to see if the right arrow key was pressed
            """Move the ship to the righht."""
            self.ship.moving_right = True #and if so we set 'moving_right' to True
        elif event.key == pygame.K_LEFT: #checks to see if the left arrow key was pressed
            """Move the ship to the left."""
            self.ship.moving_left = True #and if so we set 'moving_left' to True
        elif event.key == pygame.K_q: #checks to see if the 'Q' key was pressed
            sys.exit() #closes the game when 'Q' is pressed
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT: #checks to see if the right arrow key was pressed
            self.ship.moving_right = False #and if so we set 'moving_right' to False
        elif event.key == pygame.K_LEFT: #checks to see if the left arrow key was pressed
            self.ship.moving_left = False #and if so we set 'moving_left' to False           
    
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        self.bullets.update() #Update bullet positions.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        """Create the fleet of aliens."""
        #Create an alien and keep adding aliens until there's no room left.
        #Spacing between aliens is one alien width and one alien height.
        star = Stars(self)
        star_width, star_height = star.rect.size
        current_x, current_y = star_width, star_height
        while current_y < (self.settings.screen_height - 3 * star_height):
            while current_x < (self.settings.screen_width - 2 * star_width):
                self._create_stars(current_x, current_y)
                current_x += 2 * star_width
            #Finished a row; reset x value, and icrement y value.
            current_x = star_width
            current_y += 2 * star_height
    
    def _create_stars(self,x_position,y_position):
        """Create an alien and place it in the fleet."""
        new_star = Stars(self)
        new_star.x = x_position
        new_star.rect.x = x_position
        new_star.rect.y = y_position
        self.stars.add(new_star)
    
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.stars.draw(self.screen)
        pygame.display.flip()

if __name__ == '__main__': #only runs if the file is called directly 
    """Make a game instance, and run the game."""
    s = Star() #Create instance of the game 
    s.run_game() 