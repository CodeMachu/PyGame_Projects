import pygame

class Window():

    def __init__(self, width, height, caption):

        # Set Screen Dimensions and Caption
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)

    # Draw Image onto Screen
    # self.screen.blit(image, rect) OR window.screen.blit(image, rect)

# Window Tool
window = Window(352, 416, "Tiles Demo")