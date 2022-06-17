import pygame

from window import *

# Initialize Pygame
pygame.init()

# Update Screen
def update_screen():
    window.screen.fill((0, 0, 0))
    pygame.display.update()

# Main Method
def main():
    # Create Game Clock
    clock = pygame.time.Clock()
    FPS = 60

    while True:
        # Constant Sync of Game Clock - calculates how many frames 
        # have passed since last check and adjusts accordingly
        clock.tick(FPS)

        # Check to see if exit button has been clicked
        for event in pygame.event.get():
            # If so, terminate program
            if event.type == pygame.QUIT:
                pygame.quit()

        # Main Game Events
        update_screen()

# Run Game
if __name__ == "__main__":
    main()