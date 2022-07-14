import pygame
pygame.init()

import os


# ----------------------------------------------------------------------------------------------------

class Player():

    def __init__(self):

        # On/Off Switch
        self.is_on = False

        # Set Tile Position
        self.tile_pos = 1

        # Assign image to the tile
        self.image = pygame.image.load(os.path.join('Images', 'player.png'))

        # Create a rectangle object from the size of the image
        self.rect = self.image.get_rect()

        # Set coordinates of tile/rectangle
        self.rect.centerx = 427
        self.rect.centery = 337

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

    def update_clicked(self, mouse):

        if self.is_on:
            if self.rect.collidepoint(mouse.pos):

                # Check Left Click
                if mouse.left_clicked:
                    print(f"Player: Left Clicked")

                # Check Right Click
                if mouse.right_clicked:
                    print(f"Player: Right Clicked")

# ----------------------------------------------------------------------------------------------------

    def display(self, window):

        if self.is_on:

            # Display Surface
            window.screen.blit(self.image, self.rect)

# ----------------------------------------------------------------------------------------------------