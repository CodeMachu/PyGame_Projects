import pygame
pygame.init()

import os


# ----------------------------------------------------------------------------------------------------

class Graph():

    def __init__(self):

        print("Global Graph Tool Instantiated - Datatype: Graph() Object")

        # Create blank dictionary for storing adjacency lists of each node
        self.graph = {}

# ----------------------------------------------------------------------------------------------------

    def init_adjacency_lists(self, tilemap):

        # For each tile create an adjacency list
        for tile in tilemap.tileset:

            tile_object = tilemap.tileset[tile]

            # Start empty array for each key in the graph
            self.graph[tile] = []

            # For each tile, check if it is adjacent to the first tile
            # If it is, append it to the first tiles adjacency list
            for tile_2 in tilemap.tileset:

                tile_object_2 = tilemap.tileset[tile_2]

                # Check above tile
                if tile_object_2.rect.x == tile_object.rect.x and tile_object_2.rect.y == tile_object.rect.y - 45:
                    self.graph[tile].append(tile_object_2.id)
                # Check to the left
                if tile_object_2.rect.x == tile_object.rect.x - 45 and tile_object_2.rect.y == tile_object.rect.y:
                    self.graph[tile].append(tile_object_2.id)
                # Check to the right
                if tile_object_2.rect.x == tile_object.rect.x + 45 and tile_object_2.rect.y == tile_object.rect.y:
                    self.graph[tile].append(tile_object_2.id)
                # Check below
                if tile_object_2.rect.x == tile_object.rect.x and tile_object_2.rect.y == tile_object.rect.y + 45:
                    self.graph[tile].append(tile_object_2.id)

        # print graph values
        print("\nInstantiating Node Adjacency Dictionary")
        for node in self.graph:
            print(node, "->", self.graph[node])

# ----------------------------------------------------------------------------------------------------

    # Breadth First Search
    def bfs(self, tilemap, start_node, end_node):

        # List to keep track of visited nodes.
        visited = []

        # Initialize a queue, keep track of nodes currently in the queue.
        queue = []

        print("\nStarting Breadth First Search")
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
                        self.prev_node_dict[neighbor] = current_node                  
        '''
        print(" Printing Previous Node Dictionary:\n")
        for node in self.prev_node_dict:
            print(node, "->", self.prev_node_dict[node])
        '''
        # Return Shortest Path
        shortest_path = self.shortest_path(start_node, end_node)

        # Update Tiles
        for tile in tilemap.tiles:

            if tile.id in shortest_path:
                print(f"Tile: {tile.id} Image Updated")
                tile.image = tile.grey_tile_png

# ----------------------------------------------------------------------------------------------------