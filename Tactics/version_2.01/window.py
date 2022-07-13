import pygame
pygame.init()


# ----------------------------------------------------------------------------------------------------

# CLASS
class Window():

    def __init__(self, width, height, caption):

        print("Global Window Tool Instantiated - Datatype: Window() Object")

        # Initialize and set screen dimensions
        self.screen = pygame.display.set_mode((width, height))

        # Set caption
        pygame.display.set_caption(caption)

# To draw image onto screen, use code below
# Window.screen.blit(image, rect)

# ----------------------------------------------------------------------------------------------------