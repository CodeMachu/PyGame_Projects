import pygame

from window import *
from background import *
from mouse import *
from tiles import *
from clock import *
from fps import *
from main_menu import *
from player import *

# Initialize Pygame
pygame.init()

# Update Screen
def update_screen(window):
    # Reset Screen to Black
    window.screen.fill((0, 0, 0))
    # Background
    # background.move(window)
    # Main Menu Clicks and Display
    main_menu.detect_click(mouse, white_tilemap, player, clock)
    main_menu.display_menu(window)
    # Tilemap Clicks and Display
    white_tilemap.detect_left_click(mouse)
    white_tilemap.detect_right_click(mouse)
    white_tilemap.display_map(window)
    # Clock Display
    clock.display_time(window)
    # FPS Display
    fps.display_fps(window)
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
        update_screen(window)

# Run Game
if __name__ == "__main__":
    main()