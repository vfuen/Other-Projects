import pygame
from pygame.sprite import Sprite


class Troly(Sprite):
    """"Character and abilities"""
    def __init__(self, si_game):
        """"Inititialize Character and set start point."""
        super().__init__()
        self.screen = si_game.screen
        self.settings = si_game.settings
        self.screen_rect = si_game.screen.get_rect()


        #Load troly and get rect.
        self.image = pygame.image.load("C:\\Users\\vfuen\\Documents\\Resume\\"
                                       "Python projects\\Space Invasion\\images\\insincts3.2.bmp")
        self.rect = self.image.get_rect()

        #Start troly at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        #change the value of the characters horizon with a decimal value
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        #Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update character postion based on there movement."""
        #Update the value of x
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.troly_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.troly_speed

        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.troly_speed

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.troly_speed

        # Update the rect object from self.x and self.y

        self.rect.x = self.x
        self.rect.y = self.y




    def blitme(self):
        """Draws the troly at the current loacation"""
        self.screen.blit(self.image, self.rect)

    def troly_center(self):
        """"Put troly on the center of the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)