import pygame

class Window():

    def __init__(self, width, height, caption):

        # Set screen dimensions and caption
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)

    # Draw image onto screen with code on next line
    # self.screen.blit(image, rect) OR window.screen.blit(image, rect)

# Window Tool
window = Window(440, 440, "Tiles Demo")