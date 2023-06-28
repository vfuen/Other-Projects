import pygame.font
from pygame.sprite import Group
from troly import Troly

class Display_Score:

    def __init__(self, si_game):
        """"Record Scores."""
        self.si_game = si_game
        self.screen = si_game.screen
        self.screen_rect = self.screen.get_rect()

        self.settings = si_game.settings
        self.stats = si_game.stats

        #Settings for setting up the score.
        self.text_color = (200,20,20)
        self.font = pygame.font.SysFont(None,48)
        #Get score image ready.
        self.prepare_points()
        self.prepare_high_score()
        self.prepare_lvl()
        self.prepare_troly()
    def prepare_troly(self):
        """Display lives left on the screen."""
        self.troly = Group()
        for troly_num in range(self.stats.troly_left):
            troly = Troly(self.si_game)
            troly.rect.x = 10 +troly_num * troly.rect.width
            troly.rect.y = 10
            self.troly.add(troly)

    def prepare_lvl(self):
        """"Create a image of level"""
        lvl_str = str(self.stats.lvl)
        self.lvl_img = self.font.render(lvl_str, True, self.text_color,
                                        self.settings.bg_color)

        #Placement of level underneath points.
        self.lvl_rect = self.lvl_img.get_rect()
        self.lvl_rect.right = self.points_rect.right
        self.lvl_rect.top = self.points_rect.bottom + 20

    def prepare_high_score(self):
        """High Score becomes a displayed image."""
        high_score = round(self.stats.high_score, - 1)
        high_score_str = "{:}".format(high_score)
        self.high_score_img = self.font.render(high_score_str, True,
                 self.text_color, self.settings.bg_color)

        #Place the high score on the center of the screen.
        self.high_score_rect = self.high_score_img.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.high_score_rect.top





    def prepare_points(self):
        """Change Score into an image."""
        rounded_score = round(self.stats.points, -1)
        points_str = "{:,}".format(rounded_score)
        # points_str = str(self.stats.points)
        self.points_img = self.font.render(points_str, True,
                                          self.text_color, self.settings.bg_color)

        #Display the score on the top right corner of the screen.
        self.points_rect = self.points_img.get_rect()
        self.points_rect.right = self.screen_rect.right - 20
        self.points_rect.top = 20
        self.prepare_lvl()




    def display_points(self):
        """"Score is created onto screen."""
        self.screen.blit(self.points_img, self.points_rect)
        self.screen.blit(self.high_score_img, self.high_score_rect)
        self.screen.blit(self.lvl_img, self.lvl_rect)
        self.troly.draw(self.screen)
    def look_for_high_score(self):
        """"Looks for a high score."""
        if self.stats.points > self.stats.high_score:
            self.stats.high_score = self.stats.points
            self.prepare_high_score()