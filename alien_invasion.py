import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion():
    """General class to manage resources and the game flow."""

    def __init__(self):
        """Game initialization and its resource creation."""
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screenWidth, self.settings.ScreenHeight)
        )
        pygame.display.set_caption('Alien Invasion')

        self.ship = Ship(self)

    def runGame(self):
        """Start main loop of the game."""
        while True:
            self._checkEvents()
            self.ship.update()
            self._updateScreen()
            

    def _checkEvents(self):
        """Reaction to mouse and keyboard events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._checkKeydownEvents(event)
            elif event.type == pygame.KEYUP:
                self._checkKeyupEvents(event)

    def _checkKeydownEvents(self, event):
        """Reaction on pressing a button."""
        if event.key == pygame.K_RIGHT:
            self.ship.movingRight = True
        elif event.key == pygame.K_LEFT:
            self.ship.movingLeft = True

    def _checkKeyupEvents(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.movingRight = False
        elif event.key == pygame.K_LEFT:
            self.ship.movingLeft = False

    def _updateScreen(self):
        """Updating screen set and displaying it."""
        self.screen.fill(self.settings.bgColor)
        self.ship.blitMe()

        pygame.display.flip()

if __name__ == '__main__':
    # Create and run a game.
    ai = AlienInvasion()
    ai.runGame()