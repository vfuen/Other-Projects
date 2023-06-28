



class Settings:
    """"A class to store all settings for Alien Invaders"""

    def __init__(self):
        #Screen settings.
        self.screen_width = 1280
        self.screen_height = 1080
        self.bg_color = (0, 0, 0)
        #character Settings
        self.trolly_lives = 3
        self.troly_speed = 1.2
        self.blaster_speed = 20
        self.space_speed = .5
        self.iren_speed = .5

        # Bullet settings
        self.blaster_width = 100
        self.blaster_height = 2000
        self.blaster_color = (0, 0, 200)
        self.blasters_allowed = 10


        #Setting for speeding up parts of the game
        self.iren_drop_speed = 2
        #Faster game speed.
        self.faster_speed = 1.2

        self.points_scale = 2
        self.change_attributes()

    def change_attributes(self):
        """"Settings that change as game progression occurs."""
        self.troly_speed = 1
        self.blaster_speed = 2
        self.space_speed = 2
        self.iren_speed = .5
        # will indicate moving left while 1 will indicate moving right.
        self.iren_direction = 1.2
        #Score
        self.iren_points = 20
        #Determine the inscreased amount of points as the levels get harder.

    def faster_attributes(self):
        """"Increase the speed of characters and the amount of points
            per level difficulty"""
        self.troly_speed *= self.faster_speed
        self.iren_speed *= self.faster_speed
        self.blaster_speed *= self.faster_speed
        self.space_speed *= self.faster_speed

        self.iren_points = int(self.iren_points * self.points_scale)


