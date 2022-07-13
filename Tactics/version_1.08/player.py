import pygame
import os

# Initialize Pygame
pygame.init()

class Player():

    def __init__(self, filepath, x, y):

        print("Global Player Tool Instantiated - Datatype: Player() Object")

        # Player On/Off Switches
        self.is_on = False
        self.menu_is_on = False
        
        # Assign an image to the player
        self.image = pygame.image.load(os.path.join(filepath))

        # Create a rectangle object from the size of the image
        self.rect = self.image.get_rect()

        # Set coordinates of player
        self.rect.center = (x, y)

        # Set default tile position
        self.tile_pos = None

        # Set Default Menu Variables
        self.menu_image = pygame.image.load(os.path.join('Images/player_menu.png'))
        self.menu_rect = self.menu_image.get_rect()

    # Display Player
    def display_player(self, window):
        
        if self.is_on:
            window.screen.blit(self.image, self.rect)

    # Detect Left Click on Player
    def detect_left_click(self, mouse):

        if self.is_on:
            if mouse.left_clicked == True:

                # Get Mouse Position
                pos = pygame.mouse.get_pos()

                if self.rect.collidepoint(pos):
                    print("Player Left Clicked")

    # Detect Right Click on Player
    def detect_right_click(self, mouse):

        if self.is_on:
            if mouse.right_clicked == True:

                # Get Mouse Position
                pos = pygame.mouse.get_pos()

                if self.rect.collidepoint(pos):
                    print("Player Right Clicked\nOpening Player Menu...")

                    # Turn on Player Menu
                    self.menu_is_on = True
                    # Set position relative to mouse position
                    x, y = pos
                    self.menu_rect.top = y - 3
                    self.menu_rect.left = x - 3

    # Display Menu
    def display_menu(self, window):

        # Get Mouse Position
        pos = pygame.mouse.get_pos()

        # If mouse position does not hover over menu, it dissapears
        if self.menu_is_on:
            if self.menu_rect.collidepoint(pos) != True:
                print("Menu Not Hovered Over\nClosing Menu...")
                self.menu_is_on = False

        if self.menu_is_on:
            window.screen.blit(self.menu_image, self.menu_rect)
    
    # Return Tile Position
    def return_tile_position(self, tilemap):

        # 
        for tile in tilemap.tiles:

            if tile.rect.collidepoint(self.rect.center):
                self.tile_pos = tile.id

        print(f"Player Tile Position: {self.tile_pos}")
        return self.tile_pos