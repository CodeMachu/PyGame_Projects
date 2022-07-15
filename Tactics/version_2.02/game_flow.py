import pygame
pygame.init()

from globals import *


# ----------------------------------------------------------------------------------------------------

# Game Loop
def run_game_loop():

    while True:
        # Constant Sync of Game Clock - calculates how many frames 
        # have passed since last check and adjusts accordingly
        fps.tick()

        # Resets
        reset_all()

        # Check to see if any events have taken place
        for event in pygame.event.get():
            # QUIT, terminate program
            if event.type == pygame.QUIT:
                print("\nExit Button Clicked\nClosing Application...\n")
                pygame.quit()
            # LEFT CLICK
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse.update_clicked(event.button)
            # RIGHT CLICK
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    mouse.update_clicked(event.button)

        # Display Updates
        update_all()

# ----------------------------------------------------------------------------------------------------

# Resets
def reset_all():

    # Reset Mouse Clicked Status
    mouse.left_clicked = False
    mouse.right_clicked = False

# ----------------------------------------------------------------------------------------------------

# Display Updates
def update_all():

    # Reset Screen to Black
    window.screen.fill((0, 0, 0))
    # Mouse
    mouse.update_pos(tilemap)
    # TileMap
    tilemap.update(mouse)
    tilemap.display(window)
    # Main Menu
    main_menu.update(mouse, tilemap, player)
    main_menu.display(window, mouse)
    # FPS
    fps.update()
    fps.display(window)
    # Clock
    clock.update()
    clock.display(window)
    # Player
    player.update_clicked(mouse, tilemap)
    player.display(window)

    # Update Pygame Display
    pygame.display.update()

# ----------------------------------------------------------------------------------------------------