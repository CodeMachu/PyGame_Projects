import pygame
import random

# Tile-Color randomizer
def color_change(map):
    x = 0
    y = 0

    # Iterate through map by row
    for row in map:
        x = 0

        # Iterate each row by tile and index/ assign the corresponding image
        for tile in row:
            if x > 0 and y > 0 and x < 10 and y < 10:
                z = random.randrange(0, 270) # Increase range to decrease rate of change

                if z == 0:
                    map[x][y] = random.randrange(1, 6) # First number inclusive, Second number up to but NOT inclusive, Float is rounded down
            
            # Next Tile
            x += 1
        
        # Next Row
        y += 1