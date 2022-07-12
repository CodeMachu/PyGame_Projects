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

        # Set default tile id and text
        self.id = id
        self.text = None
        self.text_rect = None

class TileMap():

    def __init__(self, filepath_array, list):

        print("Global Tilemap Tool Instantiated - Datatype: TileMap() Object")

        # Tilemap On/Off Switch
        self.is_on = False

        # Set tile size
        self.tile_size = 45

        # An array for storing individual tiles
        self.tiles = []

        # A single surface for drawing all tiles at once
        self.surface = pygame.Surface((855, 675))
        self.rect = self.surface.get_rect()
        self.rect.topleft = 0, 0

        # For creating tile id's
        id_counter = 0
        self.font = pygame.font.SysFont('cambria', 10)

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

        # Instantiate Tiles
        self.update_tiles()

    def update_tiles(self):

        # Draw all tiles to a single surface
        for tile in self.tiles:

            tile.text = self.font.render(f'{tile.id}', True, (0, 0, 0))
            tile.text_rect = tile.text.get_rect()
            tile.text_rect.center = tile.rect.center

            self.surface.blit(tile.image, (tile.rect.x, tile.rect.y))
            self.surface.blit(tile.text, (tile.text_rect.x, tile.text_rect.y))

    # Display Tileset
    def display_map(self, window):

        if self.is_on:
            window.screen.blit(self.surface, self.rect)

    # Detect Left Click on Tile
    def detect_left_click(self, mouse, tilemap, player, graph):

        if self.is_on:
            if mouse.left_clicked == True:

                # Get Mouse Position
                pos = pygame.mouse.get_pos()

                for tile in self.tiles:

                    if tile.rect.collidepoint(pos):
                        print(f"Tile: {tile.id} Left Clicked")

                        graph.bfs(player.return_tile_position(tilemap), tilemap.return_tile_position(), tilemap)

    # Detect Right Click on Tile
    def detect_right_click(self, mouse, player):

        if self.is_on:
            if mouse.right_clicked == True:

                # Get Mouse Position
                pos = pygame.mouse.get_pos()

                for tile in self.tiles:

                    if tile.rect.collidepoint(pos):
                        print(f"Tile: {tile.id} Right Clicked")

    # Return Tile Position
    def return_tile_position(self):

        # Get Mouse Position
        pos = pygame.mouse.get_pos()

        tile_pos = None

        # 
        for tile in self.tiles:

            if tile.rect.collidepoint(pos):
                tile_pos = tile.id
                
        print(f"Tile Destination: {tile_pos}")
        return tile_pos

# Filepath Array
tiles_array = [
                'Images/blank_tile.png',
                'Images/white_tile.png'
                ]

# Starting Tilemap List
white_tile_list = [
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
            ]