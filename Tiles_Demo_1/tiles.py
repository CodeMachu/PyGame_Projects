import pygame
import os
import csv

class Tile():

    def __init__(self, csv_loc, x, y):

        # Assign an image to the tile
        self.image = pygame.image.load(os.path.join(csv_loc))

        # Create a rectangle object from the size of the image
        self.rect = self.image.get_rect()

        # Set coordinates of rectangle
        self.rect.x = x
        self.rect.y = y

        # Counting Tool
        self.counter = 0

    def move(self, window):
        self.counter += 1
        if self.counter > 3:
            self.counter = 0
        if self.counter == 3:
            self.rect.x += 1
        if self.rect.x > -1:
            self.rect.x = -440
        
        window.screen.blit(self.image, self.rect)

class TileMap():

    def __init__(self, csv_loc, images_loc):

        # Set tile size and starting coordinates
        self.tile_size = 40
        self.start_x = 0
        self.start_y = 0

        # Create map from csv
        self.map = self.read_csv(csv_loc)

        # Create list of tiles from map
        self.tiles = self.load_tiles(images_loc)

    # Read values from csv and save in a map
    def read_csv(self, csv_loc):
        map = []

        # Open File
        with open(os.path.join(csv_loc)) as file:

            # csv.reader iterates each line and returns a list of strings
            csv_data = csv.reader(file, delimiter = ',')

            # csv_data = [
            #            string,
            #            string,
            #            string
            #            ]

            # Append each string as an iterable list to the map variable
            # Passing each string into a list separates the values and makes them iterable
            for row in csv_data:
                map.append(list(row))

        return map

        # Returns values as a list of lists OR a matrix
        # map = [
        #       list[0,0,0,0,0],
        #       list[0,0,0,0,0],
        #       list[0,0,0,0,0]
        #       ]

    # Create list of tiles from map
    def load_tiles(self, images_loc):
        tiles = []

        x = 0
        y = 0
        
        # Iterate through map by row
        for row in self.map:
            x = 0

            # Iterate each row by tile and index/ assign the corresponding image
            # Coordinates are set for each tile based on the corresponding position in the matrix
            for tile in row:
                tiles.append(Tile(images_loc[int(tile)], x * self.tile_size, y * self.tile_size))

                # Next Tile
                x += 1

            # Next Row
            y += 1

        return tiles

        # Returns a list of Tile Objects
        # tiles = [
        #         Tile,
        #         Tile,
        #         Tile
        #         ]

    # Draw tiles
    def draw_tiles(self, window):
        for tile in self.tiles:
            window.screen.blit(tile.image, tile.rect)


# Image Locations Arrays
game_board_images_loc = [
                        'Map/blank_tile.png',
                        'Map/white_tile.png'
                        ]

# Game-Board TileMap
game_board = TileMap('Map/game_board.csv', game_board_images_loc)

# Stars Background
stars_bg = Tile('Map/stars.png', -440, 0)