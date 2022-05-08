import pygame

from window import *
from tiles import *

# Initialize Pygame
pygame.init()

# Load Game Board Tiles
game_board.load_tiles(game_board_images_loc)

# Update and Display Tiles
def display_tiles():
    game_board.draw_tiles(window)
    pygame.display.update()

# Main
def main():

    # Define Game Clock
    clock = pygame.time.Clock()
    FPS = 60

    # Main Loop
    while True:

        # Set Frame Rate
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Update Tiles
        display_tiles()


#
# Run Main 
if __name__ == "__main__":
    main()