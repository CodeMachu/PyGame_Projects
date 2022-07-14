import pygame
pygame.init()


# ----------------------------------------------------------------------------------------------------

class Mouse():

    def __init__(self):
        
        print("Global Mouse Tool Instantiated - Datatype: Mouse() Object")

        # Set Default Position
        self.pos = None

        # Set Default Tile Position
        self.tile_pos = None

        # Left and Right Click Switches
        self.left_clicked = False
        self.right_clicked = False

# ----------------------------------------------------------------------------------------------------

    # Update Mouse Coordinates
    def update_pos(self, tilemap):

        # Get Current Position
        self.pos = pygame.mouse.get_pos()

        # Assign Relative Tile Position
        for tile_key in tilemap.tileset:
            
            if tilemap.tileset[tile_key].rect.collidepoint(self.pos):
                self.tile_pos = tilemap.tileset[tile_key].id
                break # break once the clicked tile has been detected
            else:
                self.tile_pos = None

# ----------------------------------------------------------------------------------------------------

    # Update Mouse Clicked Status
    def update_clicked(self, event_button):

        if event_button == 1:
            self.left_clicked = True
        if event_button == 3:
            self.right_clicked = True

# ----------------------------------------------------------------------------------------------------