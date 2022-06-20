import pygame

from window import *
from background import *
from tiles import *
from clock import *
from main_menu import *

# Initialize Pygame
pygame.init()

# Update Screen
def update_screen(window):
    # Reset Screen to Black
    window.screen.fill((0, 0, 0))
    # Background Display
    background.move(window)
    # Tilemap Display
    blank_tilemap.display_map(window)
    # Clock Display
    clock.display_time(window)
    # Main Menu Display
    main_menu.display_menu(window)
    # Update Display
    pygame.display.update()

# Detect Clicking
def detect_clicks():
    # Main Menu Clicks
    main_menu.detect_click(blank_tilemap)

# Main Method
def main():
    # Create Game Clock
    clock = pygame.time.Clock()
    FPS = 60

    while True:
        # Constant Sync of Game Clock - calculates how many frames 
        # have passed since last check and adjusts accordingly
        clock.tick(FPS)

        # Check to see if any events have taken place
        for event in pygame.event.get():
            # QUIT, terminate program
            if event.type == pygame.QUIT:
                print("Exit Button Clicked")
                pygame.quit()
            # LEFT CLICK
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    print("Left Click")
                    detect_clicks()
            # RIGHT CLICK
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    print("Right Click")

        # Main Game Events
        update_screen(window)

# Run Game
if __name__ == "__main__":
    main()