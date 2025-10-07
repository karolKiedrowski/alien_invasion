import pygame

class Ship():
    """Class made for spaceship management."""

    def __init__(self, aiGame):
        """Spaceship initialization and setting its position."""
        self.screen = aiGame.screen
        self.settings = aiGame.settings
        self.screenRect = aiGame.screen.get_rect()

        # Loafing spaceship image and getting its rectangle.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Setign ship's position to middle.
        self.rect.midbottom = self.screenRect.midbottom

        # Ship float horizontal position.
        self.x = float(self.rect.x)

        # Ship movement options. 
        self.movingRight = False
        self.movingLeft = False

    def update(self):
        """Updating ship's position based on ship's movement option."""
        # Updating ship's x position, not its rect.
        if self.movingRight and self.rect.right < self.screenRect.right:
            self.x += self.settings.shipSpeed
        if self.movingLeft and self.rect.left > self.screenRect.left:
            self.x -= self.settings.shipSpeed

        # Updating rect based on self.x
        self.rect.x = self.x


    def blitMe(self):
        """Displaying spaceship in its current posiotion."""
        self.screen.blit(self.image, self.rect)