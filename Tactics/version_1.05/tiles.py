import pygame
import os

# Initialize Pygame
pygame.init()

class Tile():

    def __init__(self, id, filepath, x, y):

        # Assign an image to the tile
        self.image = pygame.image.load(os.path.join(filepath))

        # Create a rectangle object from the size of the image
        self.rect = self.image.get_rect()

        # Set coordinates of tile/rectangle
        self.rect.x = x
        self.rect.y = y

        # Set default tile id
        self.id = id

class TileMap():

    def __init__(self, filepath_array, list):

        # Tilemap On/Off Switch
        self.is_on = False

        # Set tile size and starting coordinates
        self.tile_size = 40
        self.start_x = 40
        self.start_y = 40

        # An array for storing your tileset
        self.tiles = []

        # For creating tile id's
        id_counter = 0

        y = 1

        # Iterate by Row
        for row in list:
            x = 1

            # Iterate by Value
            for value in row:
                id_counter += 1
                self.tiles.append(Tile(id_counter, filepath_array[value], x * self.tile_size, y * self.tile_size))

                # Next Tile
                x += 1

            # Next Row
            y += 1

    # Draw Tiles
    def display_map(self, window):

        if self.is_on:

            for tile in self.tiles:
                window.screen.blit(tile.image, tile.rect)

                font = pygame.font.SysFont('cambria', 10)
                text = font.render(f'{tile.id}', True, (0, 0, 0))
                #text = font.render(f'x {tile.rect.x} y {tile.rect.y}', True, (0, 0, 0))
                text_rect = text.get_rect()
                text_rect.center = tile.rect.center

                window.screen.blit(text, text_rect)


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
white_tilemap = TileMap(tiles_array, blank_map)

# Scores Tile
scores = Tile(0, 'Images/score.png', 10, 10)