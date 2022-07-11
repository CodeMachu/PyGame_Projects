# Application Start Point
import pygame

# Import global variables before importing modules that will use these globals
print("Importing Configuration...")
from config import *
create_globals()

# Import all modules
print("Importing 'from window'")
from window import *
print(window)
print("Importing 'from tiles'")
from tiles import *
print("Importing 'from fps'")
from fps import *
print("Importing 'from clock'")
from clock import *
print("Importing 'from mouse'")
from mouse import *
print("Importing 'from main_menu'")
from main_menu import *
print("Importing 'from player'")
from player import *

#from test2 import *

# Initialize Pygame
pygame.init()

# Update Screen
def update_screen():
    # Reset Screen to Black
    window.screen.fill((0, 0, 0))
    # Main Menu Clicks and Display
    main_menu.detect_click(mouse, current_tilemap, player, clock)
    main_menu.display_menu()
    # Tilemap Clicks and Display
    current_tilemap.detect_left_click(mouse)
    current_tilemap.detect_right_click(mouse)
    current_tilemap.display_map(window)
    # FPS Display
    fps.display_fps(window)
    # Clock Display
    clock.display_time(window)
    # Player CLicks and Display
    player.detect_left_click(mouse)
    player.detect_right_click(mouse)
    player.display_player(window)

    # Update Display
    pygame.display.update()

# Main Method
def main():

    while True:

        # Constant Sync of Game Clock - calculates how many frames 
        # have passed since last check and adjusts accordingly
        fps.tick()

        # Reset Click Status
        mouse.left_clicked = False
        mouse.right_clicked = False

        # Check to see if any events have taken place
        for event in pygame.event.get():
            # QUIT, terminate program
            if event.type == pygame.QUIT:
                print("Exit Button Clicked")
                pygame.quit()
            # LEFT CLICK
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse.left_click()
            # RIGHT CLICK
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    mouse.right_click()

        # Main Game Events
        update_screen()



# Run Game
if __name__ == "__main__":
    main()