import sys

import pygame

# from settings import Settings

class AlienInvasion():
    """General class to manage resources and the game flow."""

    def __init__(self):
        """Game initialization and its resource creation."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Alien Invasion')

        # defying background color
        self.bgColor = (230, 230, 230)

    def runGame(self):
        """Start main loop of the game."""
        while True:
            # Wait for key or mouse event.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Updating screen in each loop iteration
            self.screen.fill(self.bgColor)

            # Display changed screen.
            pygame.display.flip()

if __name__ == '__main__':
    # Create and run a game.
    ai = AlienInvasion()
    ai.runGame()