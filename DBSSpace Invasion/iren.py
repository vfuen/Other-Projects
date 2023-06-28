import pygame
from settings import Settings
from pygame.sprite import Sprite


class Iren(Sprite):

    def __init__(self, si_game):
        super().__init__()
        self.screen = si_game.screen
        self.settings = si_game.settings

        self.image = pygame.image.load("C:\\Users\\vfuen\\Documents\\Resume\\"
                                       "Python projects\\Space Invasion\\images\\iren3.bmp")
        self.rect = self.image.get_rect()
        # Start each new alien near the top left of the screen.

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Store the alien's exact horizontal position.

        self.x = float(self.rect.x)




    def _check_screen_edges(self):
        """"True only if iren hits the edge."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True



    def update(self):
        """"Move Iren to the right."""
        self.x += (self.settings.iren_speed *
                        self.settings.iren_direction)
        self.rect.x = self.x


    def _check_iren_bottom(self):
        """"Check to see if the squad is
         at the bottom of the screen"""
        screen_rect = self.screen.get_rect()
        for iren in self.iren.sprites():
            if iren.rect.bottom >= screen_rect.bottom:
                #Same thing happens as if trolly hit iren.
                self._troly_strikes()
                break