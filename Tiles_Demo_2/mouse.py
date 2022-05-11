import pygame
import os

class Mouse():

    def __init__(self):
        self.pos = (0, 0)
        self.get_position()

    # Get current mouse position
    def get_position(self):
        self.pos = pygame.mouse.get_pos()
        # Returns coordinates in the form of a tuple (*, *)

    # Detect if mouse collides with rectangle
    def detect_collision(self, tilemap, event):
        self.get_position()

        for tile in tilemap.tiles:
            if tile.rect.x > 0 and tile.rect.y > 0 and tile.rect.x < 400 and tile.rect.y < 400:
                if tile.rect.collidepoint(self.pos):
                    print(f'Collision at: [{tile.rect.x//40}][{tile.rect.y//40}]')

                    if event == 1:
                        print("left mouse button pressed")
                        tile.image = pygame.image.load(os.path.join('Map/blue_tile.png'))
                    if event == 3:
                        print("right mouse button pressed")
                        tile.image = pygame.image.load(os.path.join('Map/white_tile.png'))
                    

# Create Mouse 
mouse = Mouse()