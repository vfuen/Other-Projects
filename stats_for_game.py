class Stats:
    """"Statistaclly analyze the game."""

    def __init__(self, si_game):
        """Initial statistics"""

        self.settings = si_game.settings
        self.stat_reseter()

        #Inactive game state.
        self.game_active = False
        self.high_score = 0
        self.lvl = 1
    def stat_reseter(self):
        """"Finds stats that can change the game outcome."""
        self.troly_left = self.settings.trolly_lives
        self.points = 0
        self.lvl = 1