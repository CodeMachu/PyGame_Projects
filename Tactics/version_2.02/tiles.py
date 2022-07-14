import pygame
pygame.init()

import os


# ----------------------------------------------------------------------------------------------------

class Tile():

    def __init__(self, id, image, x, y):

        # Set ID
        self.id = id

        # Assign image to the tile
        self.image = image

        # Create a rectangle object from the size of the image
        self.rect = self.image.get_rect()

        # Set coordinates of tile/rectangle
        self.rect.x = x
        self.rect.y = y

        # Set default font and text for tile id label
        self.font = pygame.font.SysFont('cambria', 10)
        self.text = self.font.render(f'{self.id}', True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.rect.center

# ----------------------------------------------------------------------------------------------------

class TileMap():

    def __init__(self, tilesize, map_width, map_height):

        print("Global Tilemap Tool Instantiated - Datatype: TileMap() Object")

        # Tilemap On/Off Switches
        self.is_on = False
        self.tile_updated = False
        self.highlight_tile_is_on = False

        # Tile Images
        self.default_tile = pygame.image.load(os.path.join('Images', 'white_tile.png'))
        self.highlight_tile = pygame.image.load(os.path.join('Images', 'highlight_tile.png'))

        # Set tile size
        self.tile_size = tilesize

        # Set tilemap size (width, height)
        self.width = map_width
        self.height = map_height

        # A dictionary for storing individual tiles
        self.tileset = {}

        # A single surface for drawing all tiles at once
        self.surface = pygame.Surface((855, 675)) # same size as window
        self.surface_2 = None

        # TileMap Rectangles
        self.rect = self.surface.get_rect()
        self.rect.topleft = 0, 0
        self.highlight_tile_rect = self.highlight_tile.get_rect()
        self.highlight_tile_rect.topleft = 0, 0

        # For creating tile id's
        self.id_counter = 0

        # Generate Tilemap
        self.gen_map()

# ----------------------------------------------------------------------------------------------------

    # Generate Tilemap
    def gen_map(self):
        print("Generating TileMap...")

        self.id_counter = 0
        y = 1
        # Iterate by Row
        for row in range(1, self.height + 1):
            x = 1
            # Iterate by Tile
            for tile in range(1, self.width + 1):
                self.id_counter += 1
                self.tileset[self.id_counter] = Tile(self.id_counter, self.default_tile, x * self.tile_size, y * self.tile_size)
                # Next Tile
                x += 1
            # Next Row
            y += 1

        # Draw all tiles to surface
        for tile in self.tileset:
            self.surface.blit(self.tileset[tile].image, self.tileset[tile].rect)
            self.surface.blit(self.tileset[tile].text, self.tileset[tile].text_rect)


# ----------------------------------------------------------------------------------------------------

    # Update TileMap
    def update(self, mouse):

        if self.is_on:
            if mouse.tile_pos != None:

                self.highlight_tile_is_on = True
            
                # Check Left Click
                if mouse.left_clicked:
                    print(f"Tile: {self.tileset[mouse.tile_pos].id} Left Clicked")

                # Check Right Click
                if mouse.right_clicked:
                    print(f"Tile: {self.tileset[mouse.tile_pos].id} Right Clicked")

                # Only update surface if a tile has changed, will save A LOT of processing power each game loop
                if self.tile_updated:

                    # Reset Tilemap Surface
                    self.surface.fill((0, 0, 0))

                    # Draw all tiles to surface
                    for tile in self.tileset:
                        self.surface.blit(self.tileset[tile].image, self.tileset[tile].rect)
                        self.surface.blit(self.tileset[tile].text, self.tileset[tile].text_rect)

                # Draw Highlight Tile to Surface
                if self.highlight_tile_is_on:
                    for tile in self.tileset:
                        if self.tileset[tile].rect.collidepoint(mouse.pos):

                            self.highlight_tile_rect.center = self.tileset[tile].rect.center

            else:
                self.highlight_tile_is_on = False

        else:
            self.highlight_tile_is_on = False

# ----------------------------------------------------------------------------------------------------

    # Display TileMap
    def display(self, window):

        if self.is_on:

            # Display Surface
            window.screen.blit(self.surface, self.rect)

        if self.highlight_tile_is_on:
            
            # Display Highlight Tile
            window.screen.blit(self.highlight_tile, self.highlight_tile_rect)

# ----------------------------------------------------------------------------------------------------