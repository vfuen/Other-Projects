import pygame


class Space:

        def __init__(self, si_game):
            """"Inititialize Character and set start point."""
            self.screen = si_game.screen
            self.screen_rect = si_game.screen.get_rect()
            self.settings = si_game.settings

            # Load troly and get rect.
            self.image = pygame.image.load("C:\\Users\\vfuen\\Documents\\Resume\\"
                                           "Python projects\\Space Invasion\\images\\space2.bmp")
            self.rect = self.image.get_rect()

            # Start troly at the bottom center of the screen
            self.rect.midbottom = self.screen_rect.midbottom


            self.x = float(self.rect.x)
            # Movement flag
            self.moving_right = False
            self.moving_left = False

        def update(self):
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.x += self.settings.space_speed
            if self.moving_left and self.rect.left > 0:
                self.x -= self.settings.space_speed

            self.rect.x = self.x
        def blitme(self):
            """Draws the troly at the current loacation"""
            self.screen.blit(self.image, self.rect)

