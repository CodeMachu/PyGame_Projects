# Application Start Point
import pygame

# Initialize Pygame
pygame.init()

# Import and Instantiate Global Tools
print("Instantiating Global Tools...")
from config import window
from config import mouse
from config import tilemap
from config import fps
from config import clock
from config import main_menu
from config import player
from config import graph

# Update Screen
def update_screen():
    # Reset Screen to Black
    window.screen.fill((0, 0, 0))
    # Main Menu Clicks and Display
    main_menu.detect_click(mouse, tilemap, clock, player)
    main_menu.display_menu(window)
    # Tilemap Clicks and Display
    tilemap.detect_left_click(mouse)
    tilemap.detect_right_click(mouse)
    #tilemap.display_map(window)
    tilemap.display_path(window, tilemap, player, graph)
    # FPS Display
    fps.display_fps(window)
    # Clock Display
    clock.display_time(window)
    # Player CLicks and Display
    player.detect_left_click(mouse)
    player.detect_right_click(mouse)
    player.display_player(window)
    player.display_menu(window)

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