import sys
from time import sleep
import pygame

from settings import Settings
from stats_for_game import Stats
from play_button import Play_Button

from score_display import Display_Score
from troly import Troly
from blaster import Blaster
from space import Space
from iren import Iren


class SpaceInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height), pygame.FULLSCREEN)
        pygame.display.set_caption("The Aliens are Coming!")

        #The storage of game sats and the points for the game.
        self.stats = Stats(self)
        self.dp = Display_Score(self)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height


        self.iren = pygame.sprite.Group()
        self.troly = Troly(self)
        self._create_squad()
        self._create_iren(2,2)




        self.blasters = pygame.sprite.Group()
        self.space = Space(self)
        WHITE = (255, 255, 255)
        self.screen.fill(WHITE)
        self.YELLOW = (249, 215, 28)
        #Play Button create
        self.play_button = Play_Button(self, "Play Now")

    def run_game(self):
            """Start the main loop for the game."""
            while True:
                self._check_events()
                if self.stats.game_active:
                     self.space.update()
                     self.troly.update()

                     self._update_iren()

                     self._update_blasters()

                self._update_screen()

    def _troly_strikes(self):
       """" Iren colliding with Troly response."""
       if self.stats.troly_left > 0:




        #Loss of troly
        self.stats.troly_left -= 1
        self.dp.prepare_troly()
        self.dp.prepare_points()
        #Remove Iren and blasts
        self.iren.empty()
        self.blasters.empty()

        #New Squad appears and troly is placed in the center.
        self._create_squad()
        self.troly.troly_center()
        self.settings.faster_attributes()
        #Delay.
        sleep(.2)

       else:
           self.stats.game_active = False
           pygame.mouse.set_visible(True)


    def _create_squad(self):
        iren = Iren(self)
        iren_width, iren_height = iren.rect.size
        available_space_x = self.settings.screen_width - (2 * iren_width)
        number_irens_x = available_space_x // (2 * iren_width)

        #Find out the number of irens that fit on the screen.
        troly_height = self.troly.rect.height
        available_space_y = (self.settings.screen_height -
                             (2 * iren_height) - troly_height)
        number_rows = available_space_y // (2 * iren_height)

        for row_number in range(number_rows):
            for iren_number in range(number_irens_x):
                self._create_iren(iren_number, row_number)



    def _create_iren(self, iren_number, row_number):

        iren = Iren(self)
        iren_width, iren_height = iren.rect.size
        iren.x = iren_width + 2 * iren_width * iren_number
        iren.rect.x = iren.x
        iren.rect.y = iren.rect.height + 2 * iren.rect.height * row_number
        self.iren.add(iren)

    def _check_iren_edges(self):
        """Changes direction when iren gets to the edge."""
        for iren in self.iren.sprites():
            if iren._check_screen_edges():
                self._change_iren_direction()
                break

    def _change_iren_direction(self):
        """"Drops all th irens to the next row and changes direction."""
        for iren in self.iren.sprites():
            iren.rect.y += self.settings.iren_drop_speed
        self.settings.iren_direction *= -1

    def _check_iren_bottom(self):
        """"Check to see if the squad is
         at the bottom of the screen"""
        screen_rect = self.screen.get_rect()
        for iren in self.iren.sprites():
            if iren.rect.bottom >= screen_rect.bottom:
                # Same thing happens as if troly hit iren.
                self._troly_strikes()
                break

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                self._click_play_button(mouse_position)

    # def _press_key_p(self):
    #     """"Initialize the game when pressing the letter p."""
    #     # press_p = pygame.K_p
    #     # if press_p and not self.stats.game_active:
    #     # self.settings.change_attributes()
    #     self.stats.stat_reseter()
    #     self.stats.game_active = True
    #     # self.dp.prepare_points()

            # Remove iren and blasts.
        # self.iren.empty()
        # self.blasters.empty()
        #
        #     # Create the squad and place them in the center
        # self._create_squad()
        # self.troly.troly_center()
        # pygame.mouse.set_visible(False)




    def _click_play_button(self, mouse_position):
        """"Starts game after play is clicked."""

        clicks_button = self.play_button.rect.collidepoint(mouse_position)
        if clicks_button and not self.stats.game_active:

            #Reset the game.
            self.settings.change_attributes()
            self.stats.stat_reseter()
            self.stats.game_active = True
            self.dp.prepare_points()
            self.dp.prepare_lvl()
            self.dp.prepare_troly()


            #Remove iren and blasts.
            self.iren.empty()
            self.blasters.empty()

            #Create the squad and place them in the center
            self._create_squad()
            self.troly.troly_center()
            #Hide mouse cursor when games starts.
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.troly.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.troly.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_blaster()
        elif event.key == pygame.K_UP:
            self.troly.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.troly.moving_down = True
        # elif event.key == pygame.K_p:
        #     self._press_key_p()
        # elif event.key == pygame.K_e:
        #     self._press_key_p()




    # def _check_mouse_events(self, event):
    #    mouse_position = pygame.mouse.get_pos()
    #    self._click_play_button(mouse_position)


    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.troly.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.troly.moving_left = False

        elif event.key == pygame.K_UP:
            self.troly.moving_up = False

        elif event.key == pygame.K_DOWN:
            self.troly.moving_down = False

    def _fire_blaster(self):
        """Create a new blast and add it to the blasts group."""
        if len(self.blasters) < self.settings.blasters_allowed:
            new_blaster = Blaster(self)
            self.blasters.add(new_blaster)

    def _update_blasters(self):
        """Update position of blast and get rid of old blasters."""
        # Update blast positions.
        self.blasters.update()

        # Get rid of blasts that have disappeared.
        for blaster in self.blasters.copy():
            if blaster.rect.bottom <= 0:
                 self.blasters.remove(blaster)

        self._check_blast_encounter()


    def _check_blast_encounter(self):
        """" Checks checks to see if a blast hits iren."""""
        #If a blast hits iren both the blast and iren disapear.


        collisions = pygame.sprite.groupcollide(
            self.blasters, self.iren, True, True)

        if collisions:
            for iren in collisions.values():
                self.stats.points += self.settings.iren_points * len(iren)
                self.dp.prepare_points()
                self.dp.look_for_high_score()
        if not self.iren:
            self.blasters.empty()
            self._create_squad()
            self.settings.faster_attributes()
            #Level increasment
            self.stats.lvl +=1
            self.dp.prepare_lvl()


    def _update_iren(self):

        """
        Checks to see if the squad is at the edge.
        Then updates the positions of all irens in the squad."""
        self._check_iren_edges()

        self.iren.update()

        if pygame.sprite.spritecollideany(self.troly, self.iren):
            self._troly_strikes()



        self._check_iren_bottom()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""


        self.screen.fill(self.settings.bg_color)
        # Draw button and message onto screen.
        self.space.blitme()

        for blaster in self.blasters.sprites():
            blaster.draw_blaster()

        self.troly.blitme()
        self.iren.draw(self.screen)
        self.dp.display_points()



        if not self.stats.game_active:
            self.play_button.draw_button()
        # pygame.draw.circle(self.screen, self.YELLOW, (2400, 860), 5, 0)
        # pixObj = pygame.PixelArray(self.screen)





        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    si = SpaceInvasion()
    si.run_game()