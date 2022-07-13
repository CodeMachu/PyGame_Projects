import pygame
pygame.init()

from window import Window
from fps import FPS
from clock import Clock
from mouse import Mouse


# ----------------------------------------------------------------------------------------------------

# Initialize Global Variables
def init_globals():

    global window
    window = Window(855, 675, "Version_2.01")

    global fps
    fps = FPS()

    global clock
    clock = Clock()

    global mouse
    mouse = Mouse()

# ----------------------------------------------------------------------------------------------------

# Initialize Global Variables
init_globals()

# ----------------------------------------------------------------------------------------------------