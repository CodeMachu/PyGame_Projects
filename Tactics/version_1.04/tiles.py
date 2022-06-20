import pygame
import os

# Initialize Pygame
pygame.init()

class Tile():

    def __init__(self, filepath, x, y):

        # Assign an image to the tile
        self.image = pygame.image.load(os.path.join(filepath))

        # Create a rectangle object from the size of the image
        self.rect = self.image.get_rect()

        # Set coordinates of rectangle
        self.rect.x = x
        self.rect.y = y

class TileMap():

    def __init__(self, filepath, list):

        # Tilemap On/Off Switches
        self.is_on = False

        # Set tile size and starting coordinates
        self.tile_size = 40
        self.start_x = 40
        self.start_y = 40

        self.tiles = []

        y = 1

        # Iterate by Row
        for row in list:
            x = 1

            # Iterate by Value
            for value in row:
                self.tiles.append(Tile(filepath[value], x * self.tile_size, y * self.tile_size))
                        
                # Next Tile
                x += 1

            # Next Row
            y += 1

    # Draw Tiles
    def display_map(self, window):

        if self.is_on:

            for tile in self.tiles:
                window.screen.blit(tile.image, tile.rect)

# Filepath Array
tiles_array = [
                'Images/blank_tile.png',
                'Images/white_tile.png'
                ]

# Starting Tilemap List
blank_map = [
                [1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1]
            ]

# Starting Tilemap
blank_tilemap = TileMap(tiles_array, blank_map)


