import pygame

from window import *
from tiles import *
from background import *
from colorchange import *

# Initialize pygame
pygame.init()

# Load game board tiles
game_board.load_tiles(game_board_images_loc)
                    
# Update and display tiles
def update_tiles():
    stars_bg.move(window)
    color_change(game_board.map)
    game_board.load_tiles(game_board_images_loc)
    game_board.draw_tiles(window)
    pygame.display.update()

# Main
def main():

    # Define game clock
    clock = pygame.time.Clock()
    FPS = 60

    # Main loop
    while True:

        # Set frame rate
        clock.tick(FPS)

        # Check if the quit button has been pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Update tiles
        update_tiles()


#
# Run main 
if __name__ == "__main__":
    main()