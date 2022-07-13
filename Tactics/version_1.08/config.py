import pygame
from graph import Graph

from window import Window
from mouse import Mouse
from tiles import TileMap, white_tile_list
from fps import FPS
from clock import Clock
from main_menu import MainMenu
from player import Player

# Initialize Pygame
pygame.init()

# Create Global Variables
def create_globals():
    
    global window
    window = Window(855, 675, "Graph Algorithms")

    global mouse
    mouse = Mouse()

    global tilemap
    tilemap = TileMap(white_tile_list)

    global fps
    fps = FPS()

    global clock
    clock = Clock()

    global main_menu
    main_menu = MainMenu()

    global player
    player = Player('Images/player.png', 427, 337)

    global graph
    graph = Graph(tilemap)

# Instantiate Globals
create_globals()