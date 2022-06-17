import pygame

from tiles import Tile

class Background(Tile):

    def __init__(self, csv_loc, x, y):
        super().__init__(csv_loc, x, y)

        self.counter = 0

    def move(self, window):
        self.counter += 1
        if self.counter > 4: # Increase counter to decrease velocity
            self.counter = 0
        if self.counter == 4:
            self.rect.x += 1
        if self.rect.x > -1:
            self.rect.x = -440
        
        window.screen.blit(self.image, self.rect)

# Stars Background
stars_bg = Background('Map/stars.png', -440, 0)