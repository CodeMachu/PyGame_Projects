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

    def __init__(self):

        # Set tile size and starting coordinates
        self.tile_size = 40
        self.start_x = 0
        self.start_y = 0
