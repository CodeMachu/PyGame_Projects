import pygame
from tiles import *

# Initialize Pygame
pygame.init()

class Graph():

    def __init__(self, tilemap):

        # Create Blank Dictionary 
        self.graph = {}

        # For each tile create an adjacency list
        for tile in tilemap.tiles:

            key = tile.id

            # Start empty array for each key in the graph
            self.graph[key] = []

            # For each tile, check if it is adjacent to the first tile
            # If it is, append it to the first tiles adjacency list
            for tile_2 in tilemap.tiles:

                # Check above tile
                if tile_2.rect.x == tile.rect.x and tile_2.rect.y == tile.rect.y - 45:
                    self.graph[key].append(tile_2.id)
                # Check to the left
                if tile_2.rect.x == tile.rect.x - 45 and tile_2.rect.y == tile.rect.y:
                    self.graph[key].append(tile_2.id)
                # Check to the right
                if tile_2.rect.x == tile.rect.x + 45 and tile_2.rect.y == tile.rect.y:
                    self.graph[key].append(tile_2.id)
                # Check below
                if tile_2.rect.x == tile.rect.x and tile_2.rect.y == tile.rect.y + 45:
                    self.graph[key].append(tile_2.id)

        # print graph values
        print("\nNode Adjacency Dictionary")
        for node in self.graph:
            print(node, "->", self.graph[node])

        # Dictionary for tracking previous node of a node
        self.prev_node_dict = {}

    # Breadth First Search
    def bfs(self, start_node, end_node):

        # List to keep track of visited nodes.
        visited = []

        # Initialize a queue, keep track of nodes currently in the queue.
        queue = []

        print("\nStarting BFS")
        visited.append(start_node)
        queue.append(start_node)

        while queue:                                    # while queue contains values
            current_node = queue.pop(0)                 # pop the value at the front of the queue (the top of the list), the pop() method returns removed value.
            if current_node != end_node:                # If destination node reached, end loop

                # for each neighbor of current node
                for neighbor in self.graph[current_node]:

                    if neighbor not in visited:
                        
                        # append arrays and prev node graph
                        visited.append(neighbor)
                        queue.append(neighbor)
                        self.prev_node[neighbor] = current_node                  

        print("\nPrevious Node Dictionary:\n")
        for node in self.prev_node:
            print(node, "->", self.prev_node[node])

    # Find Shortest Path
    def shortest_path(self, start_node, end_node):

        # Create an empty array for backward path order
        backward_path = []

        # Set current node to end node
        current_node = end_node

        # Work backwards through the Prev_Node Graph until you reach the start node
        while current_node != start_node:

            backward_path.append(current_node)
            current_node = self.prev_node[current_node]

        # Correct Path Order
        backward_path.reverse()

        print("\nShortest Path")
        print(backward_path)

        return backward_path


# Graph Tool
game_graph = Graph(white_tilemap)