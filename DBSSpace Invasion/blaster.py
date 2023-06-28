import pygame
from pygame.sprite import Sprite


class Blaster(Sprite):
    """A class to manage blasters fired from the ship"""

    def __init__(self, si_game):
        """Create a blaster object at the ship's current position."""
        super().__init__()
        self.screen = si_game.screen
        self.settings = si_game.settings
        self.color = self.settings.blaster_color

        # Create a blaster rect at (0, 100) and then set correct position.
        self.rect = pygame.Rect(0, 100, self.settings.blaster_width,
                                self.settings.blaster_height)
        self.rect.midtop = si_game.troly.rect.midtop

        # Store the blasters' position as a decimal value.
        self.y = float(self.rect.y)

    def update(self):
        """Move the blaster up the screen."""
        # Update the decimal position of the blaster.
        self.y -= self.settings.blaster_speed
        # Update the rect position.
        self.rect.y = self.y

    def draw_blaster(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)