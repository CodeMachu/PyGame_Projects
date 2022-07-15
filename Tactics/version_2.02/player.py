import pygame
pygame.init()

import os


# ----------------------------------------------------------------------------------------------------

class Player():

    def __init__(self):

        # On/Off Switch
        self.is_on = False
        self.menu_on = False

        # Set Tile Position
        self.tile_pos = 1

        # Assign image to the tile
        self.image = pygame.image.load(os.path.join('Images', 'player.png'))

        # Create a rectangle object from the size of the image
        self.rect = self.image.get_rect()

        # Set coordinates of tile/rectangle
        self.rect.topleft = 405, 315

        # Set Default Menu Variables
        self.menu_image = pygame.image.load(os.path.join('Images/player_menu.png'))
        self.menu_rect = self.menu_image.get_rect()

# ----------------------------------------------------------------------------------------------------

    def move(self, tilemap, x, y):

        if self.is_on:

            self.rect.centerx = x
            self.rect.centery = y

            self.update_pos(tilemap)

            print("\nUpdating Player Position...\nMoving Player...")

# ----------------------------------------------------------------------------------------------------

    def update_pos(self, tilemap):

        if self.is_on:

            # Assign Relative Tile Position
            for tile_key in tilemap.tileset:
                
                if tilemap.tileset[tile_key].rect.collidepoint(self.rect.center):
                    self.tile_pos = tilemap.tileset[tile_key].id
                    break # break once the clicked tile has been detected
                else:
                    self.tile_pos = None

    def update_clicked(self, mouse, tilemap):

        if self.is_on:
            if self.rect.collidepoint(mouse.pos):

                # Check Left Click
                if mouse.left_clicked:
                    print(f"Player: Left Clicked")

                # Check Right Click
                if mouse.right_clicked:
                    print(f"Player: Right Clicked")
                    
                    print("Player Menu: ON")
                    self.menu_on = True
                    tilemap.highlight_tile_is_on = False
                    print(f"Highlight Tile Is On = {tilemap.highlight_tile_is_on}")
                    x, y = mouse.pos
                    self.menu_rect.top = y - 3
                    self.menu_rect.left = x - 3

        # If mouse position does not hover over menu, it dissapears
        if self.menu_on:

            if self.menu_rect.collidepoint(mouse.pos) != True:
                print("Menu Not Hovered Over\nClosing Player Menu...")
                self.menu_on = False
                tilemap.highlight_tile_is_on = True

# ----------------------------------------------------------------------------------------------------

    def display(self, window):

        if self.is_on:

            # Display Surface
            window.screen.blit(self.image, self.rect)

        if self.menu_on:

            # Display Player Menu
            window.screen.blit(self.menu_image, self.menu_rect)

# ----------------------------------------------------------------------------------------------------