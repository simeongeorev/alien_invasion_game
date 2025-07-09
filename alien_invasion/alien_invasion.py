import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()

        # Create an object to help track time
        self.clock = pygame.time.Clock()

        # Create an instance of class Settings
        self.settings = Settings()

        # Sets the resolution
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Create an instance of class Ship
        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

            # Sets the frame rate to 60 frames per second
            self.clock.tick(60) # might be moved to _update_screen as well

    def _check_events(self):
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True
                    if event.key == pygame.K_LEFT:
                        self.ship.moving_left = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False
                    if event.key == pygame.K_LEFT:
                        self.ship.moving_left = False

    def _update_screen(self):
        # Redraw the screen with the set color during each pass through the loop.
        self.screen.fill(self.settings.bg_color)

        # Draws the ship on the screen
        self.ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
