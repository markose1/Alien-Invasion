import sys
import pygame
from settings6 import Settings
from raindrop5 import Raindrops

class Raindrop:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Rain")
        self.raindrops = pygame.sprite.Group()
        self._create_rain()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_raindrops()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_q:
            sys.exit()      

    def _update_raindrops(self):
        """Update the positions of all aliens in the fleet."""
        """Check if the fleet is at an edge, then update positions."""
        self._check_rain_edges()
        self.raindrops.update()

    def _create_rain(self):
        """Create the fleet of aliens."""
        # Create an alien and keep adding aliens until there's no room left.
        # Spacing between aliens is one alien width and one alien height.
        raindrop = Raindrops(self)
        raindrop_width, raindrop_height = raindrop.rect.size

        current_x, current_y = raindrop_width, raindrop_height
        while current_y < (self.settings.screen_height - 3 * raindrop_height):
            while current_x < (self.settings.screen_width - 2 * raindrop_width):
                self._create_raindrop(current_x, current_y)
                current_x += 2 * raindrop_width

            # Finished a row; reset x value, and increment y value.
            current_x = raindrop_width
            current_y += 2 * raindrop_height

    def _create_raindrop(self, x_position, y_position):
        """Create an alien and place it in the fleet."""
        rain = Raindrops(self)
        rain.x = x_position
        rain.rect.x = x_position
        rain.rect.y = y_position
        self.raindrops.add(rain)

    def _check_rain_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for drops in self.raindrops.sprites():
            if drops.check_edges():
                self._change_rain_direction()
                break

    def _change_rain_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for drops in self.raindrops.sprites():
            drops.rect.y += self.settings.raindrop_speed
        self.settings.rain_direction *= -1

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.raindrops.draw(self.screen)
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    r = Raindrop()
    r.run_game()