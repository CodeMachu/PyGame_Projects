import pygame

class Window():

    def __init__(self, width, height, caption):

        # Set screen dimensions
        self.screen = pygame.display.set_mode((width, height))

        # Set caption
        pygame.display.set_caption(caption)

# Window Tool
window = Window(440, 440, "Tactics")

# To draw image onto screen, use code below
# window.screen.blit(image, rect)