class Settings:
    def __init__(self):
        """Settings for the game"""

        self.width = 1200
        self.height = 800
        self.background_color = (0, 0, 0)
        self.caption = "Alien Invaders"
        self.frame_rate = 60

        # Ship
        self.ship_speed = 1.5
        self.ship_scale = 0.1

        # Bullets
        self.bullet_speed = 5
        self.bullet_width = 3
        self.bullet_height = 30
        self.bullet_color = (255, 0, 0)
        self.maximum_number_of_bullets = 6

        # Alien
        self.alien_scale = 0.1
        self.alien_spacing = 50

