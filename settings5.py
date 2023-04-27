class Settings:
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        #Ship settings
        self.ship_speed = 5.5 #the ships position is adjusted by 1.5 pixels each 
        self.ship_limit = 3 
        #Bullet settings
        self.bullet_speed = 7.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 10