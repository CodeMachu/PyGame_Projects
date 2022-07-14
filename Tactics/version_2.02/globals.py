import pygame
pygame.init()

from window import Window
from mouse import Mouse
from fps import FPS
from clock import Clock
from main_menu import MainMenu
from tiles import TileMap
from player import Player
from graph import Graph


# ----------------------------------------------------------------------------------------------------

# Initialize Global Variables
def init_globals():

    global window
    window = Window(855, 675, "Version_2.01")

    global mouse
    mouse = Mouse()

    global player 
    player = Player()

    global fps
    fps = FPS()

    global clock
    clock = Clock()

    global main_menu
    main_menu = MainMenu()

    global tilemap
    tilemap = TileMap(45, 17, 13)

    global graph
    graph = Graph()
    graph.init_adjacency_lists(tilemap)

# ----------------------------------------------------------------------------------------------------

# Initialize Global Variables
init_globals()

# ----------------------------------------------------------------------------------------------------