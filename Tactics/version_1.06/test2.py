from tiles import *

# CREATE GRAPH using Tileset
# A Graph is represented using an Adjacency List
# An easy way to do this in Python is to use a dictionary data structure, where each node has a stored list of its adjacent nodes.

def create_graph(tilemap):

    # Create Blank Dictionary
    graph = {}
    
    for tile in tilemap.tiles:
        key = tile.id

        # start empty array for each key
        graph[key] = []

        for tile_2 in tilemap.tiles:
            # Check above tile
            if tile_2.rect.x == tile.rect.x and tile_2.rect.y == tile.rect.y - 45:
                graph[key].append(tile_2.id)
            # Check to the left
            if tile_2.rect.x == tile.rect.x - 45 and tile_2.rect.y == tile.rect.y:
                graph[key].append(tile_2.id)
            # Check to the right
            if tile_2.rect.x == tile.rect.x + 45 and tile_2.rect.y == tile.rect.y:
                graph[key].append(tile_2.id)
            # Check below
            if tile_2.rect.x == tile.rect.x and tile_2.rect.y == tile.rect.y + 45:
                graph[key].append(tile_2.id)

    return graph

# Create Graph
graph = create_graph(white_tilemap)

# print graph values
print("\nNode Adjacency Dictionary...")
for node in graph:
    print(node, "->", graph[node])

#
visited = []   # List to keep track of visited nodes.
queue = []     # Initialize a queue, keep track of nodes currently in the queue.

#
prev_node = {} # Dictionary for tracking previous node of a node

# Function for BFS
def breadth_first_search(graph, visited, start_node, end_node):
    print("\nStarting BFS")
    visited.append(start_node)
    queue.append(start_node)

    while queue:                                    # while queue contains values

        current_node = queue.pop(0)                 # pop the value at the front of the queue (the top of the list), the pop() method returns removed value.

        if current_node != end_node:                # If destination node reached, end loop

            # for each neighbor of current node
            for neighbor in graph[current_node]:

                if neighbor not in visited:
                    
                    # append arrays and prev node graph
                    visited.append(neighbor)
                    queue.append(neighbor)
                    prev_node[neighbor] = current_node                  

    print("Previous Node Dictionary:")
    for node in prev_node:
        print(node, "->", prev_node[node])

    return visited

# Run BFS and assign array to a variable
bfs = breadth_first_search(graph, visited, 1, 221)

def find_shortest_path(start_node, end_node):

    # Create an empty array for backward path order
    backward_path = []

    # Set current node to end node
    current_node = end_node

    # Work backwards through the Prev_Node Graph until you reach the start node
    while current_node != start_node:

        backward_path.append(current_node)
        current_node = prev_node[current_node]

    # Correct Path Order
    backward_path.reverse()

    print("\nShortest Path")
    print(backward_path)

    return backward_path

def highlight_path(tilemap, path):

    grey_tile = pygame.image.load(os.path.join("Images/grey_tile.png"))

    for tile in tilemap.tiles:

        if tile.id in path:

            tile.image = grey_tile

highlight_path(white_tilemap, find_shortest_path(1, 221))
