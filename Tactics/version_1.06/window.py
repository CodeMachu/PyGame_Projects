import pygame
from config import *

class Window():

    def __init__(self, width, height, caption):

        # Initialize and set screen dimensions
        self.screen = pygame.display.set_mode((width, height))

        # Set caption
        pygame.display.set_caption(caption)

# Global Window Tool
window = Window(855, 675, "Graph Algorithms")
print(f"Global Window Parameters Set:\n   - Width: 855\n   - Height: 675\n    - Caption: Graph Algorithms")
# To draw image onto screen, use code below
# window.screen.blit(image, rect)