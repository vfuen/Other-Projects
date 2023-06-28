import pygame.font

class Play_Button:
    def __init__(self, si_game, msg):
        """"Initialize button attributes."""
        self.screen = si_game.screen
        self.screen_rect = self.screen.get_rect()

        #Dimensions and properties of the button.
        self.width, self.height = 250, 100
        self.button_color = (100,100,100)
        self.text_color = (0,200,200)
        self.font = pygame.font.SysFont(None, 60,)

        #Make a button as a rect object
        # and put it on the center of the screen.
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #Prepare a button message one time.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
            """"Transforming message into a button
            and placing text on the center"""
            self.msg_image = self.font.render(msg, True, self.text_color,
                                              self.button_color)
            self.msg_image_rect = self.msg_image.get_rect()
            self.msg_image_rect.center = self.rect.center

    def draw_button(self):
            #Draws the button and a message.
            self.screen.fill(self.button_color, self.rect)
            self.screen.blit(self.msg_image, self.msg_image_rect)
