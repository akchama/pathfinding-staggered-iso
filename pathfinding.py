import math
from constants import TILE_WIDTH, TILE_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT

MAX_COLS = (SCREEN_WIDTH // (TILE_WIDTH // 2)) + 1
MAX_ROWS = (SCREEN_HEIGHT // (TILE_HEIGHT // 2)) + 1

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.g = 0
        self.h = 0
        self.f = 0
        self.parent = None

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

def get_neighbors(node):
    if node.y % 2 == 0:  # Even rows
        neighbors = [
            Node(node.x-1, node.y-1),  # Top-left diagonal
            Node(node.x, node.y-1),    # Top-right diagonal
            Node(node.x-1, node.y+1),  # Bottom-left diagonal
            Node(node.x, node.y+1)     # Bottom-right diagonal
        ]
    else:  # Odd rows
        neighbors = [
            Node(node.x, node.y-1),    # Top-left diagonal
            Node(node.x+1, node.y-1),  # Top-right diagonal
            Node(node.x, node.y+1),    # Bottom-left diagonal
            Node(node.x+1, node.y+1)   # Bottom-right diagonal
        ]
    return neighbors

def heuristic(node1, node2):
    # Using Euclidean distance as the heuristic since only diagonal moves are allowed
    return math.sqrt((node1.x - node2.x) ** 2 + (node1.y - node2.y) ** 2)

def get_diagonal_neighbors(node):
    # Diagonal neighbors for the staggered isometric map
    neighbors = get_neighbors(node)
    return neighbors

def a_star(start, end):
    open_list = []
    closed_list = []
    open_list.append(start)

    while open_list:
        current_node = min(open_list, key=lambda x: x.f)

        if current_node == end:
            path = []
            while current_node:
                path.append((current_node.x, current_node.y))
                current_node = current_node.parent
            return path[::-1]

        open_list.remove(current_node)
        closed_list.append(current_node)

        neighbors = get_diagonal_neighbors(current_node)

        for neighbor in neighbors:
            # Use the constants MAX_COLS and MAX_ROWS
            if neighbor.x < 0 or neighbor.x >= MAX_COLS or neighbor.y < 0 or neighbor.y >= MAX_ROWS:
                continue

            if neighbor in closed_list:
                continue

            tentative_g = current_node.g + 1
            if neighbor in open_list:
                if tentative_g < neighbor.g:
                    neighbor.g = tentative_g
                    neighbor.h = heuristic(neighbor, end)
                    neighbor.f = neighbor.g + neighbor.h
                    neighbor.parent = current_node
            else:
                neighbor.g = tentative_g
                neighbor.h = heuristic(neighbor, end)
                neighbor.f = neighbor.g + neighbor.h
                neighbor.parent = current_node
                open_list.append(neighbor)

    print(f"Failed to find a path from {start.x},{start.y} to {end.x},{end.y}")
    return None
