import pygame

class Window():

    def __init__(self, width, height, caption):

        # Set screen dimensions
        self.screen = pygame.display.set_mode((width, height))

        # Set caption
        pygame.display.set_caption(caption)

    # To draw image onto screen, use code on next line
    # self.screen.blit(image, rect) OR window.screen.blit(image, rect)

# Window Tool
window = Window(800, 720, "Tactics")