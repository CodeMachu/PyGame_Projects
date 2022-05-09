import pygame
import os
import csv

class Tile():

    def __init__(self, csv_loc, x, y):

        # Assign an Image to the Tile
        self.image = pygame.image.load(os.path.join(csv_loc))

        # Create a Rectangle Object from the size of the Image
        self.rect = self.image.get_rect()

        # Set Coordinates of Rectangle
        self.rect.x = x
        self.rect.y = y

class TileMap():

    def __init__(self, csv_loc, images_loc):

        # Set Tile Size and Starting Coordinates
        self.tile_size = 32
        self.start_x = 0
        self.start_y = 0

        # Create Map from CSV
        self.map = self.read_csv(csv_loc)

        # Create List of Tiles from Map
        self.tiles = self.load_tiles(images_loc)

    # Read Values from CSV and Save in a Map
    def read_csv(self, csv_loc):
        map = []

        # Open File
        with open(os.path.join(csv_loc)) as data:

            # Read File/ Save CSV data as a List of Strings
            file = csv.reader(data, delimiter = ',')

            # file = [
            #        string,
            #        string,
            #        string
            #        ]

            # Transform and Append each String as an iterable List OR Array to the map variable
            for row in file:
                map.append(list(row))

        return map

        # Returns Values as an Array of Arrays OR a List of Rows OR a Matrix
        # map = [
        #       list[0,0,0,0,0],
        #       list[0,0,0,0,0],
        #       list[0,0,0,0,0],
        #       list[0,0,0,0,0]
        #       ]

    # Create List of Tiles from Map
    def load_tiles(self, images_loc):
        tiles = []

        x = 0
        y = 0
        
        # Iterate through Map by Row
        for row in self.map:
            x = 0

            # Iterate each Row by Tile and Index the corresponding Image in the appropriate Array
            for tile in row:
                tiles.append(Tile(images_loc[int(tile)], x * self.tile_size, y * self.tile_size))

                # Next Tile
                x += 1

            # Next Row
            y += 1

        return tiles

    # Draw Tiles
    def draw_tiles(self, window):
        for tile in self.tiles:
            window.screen.blit(tile.image, tile.rect)


# CSV Locations
game_board_csv_loc = 'Map/game_board.csv'

# Image Locations
gb0 = 'Map/black_tile.png'
gb1 = 'Map/white_tile.png'

# Image Locations Arrays
game_board_images_loc = [
                        gb0,
                        gb1
                        ]

# Game-Board TileMap
game_board = TileMap(game_board_csv_loc, game_board_images_loc)