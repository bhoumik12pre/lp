import heapq

# Define a Node class to store information about each position on the grid
class Node:
    def __init__(self, position, parent=None):
        self.position = position  # Position is a tuple (x, y)
        self.parent = parent  # Parent node to trace the path back
        self.g = 0  # Cost to reach this node from the start
        self.h = 0  # Heuristic (estimated cost to the goal)
        self.f = 0  # Total cost (f = g + h)

    # Comparison function to allow Node objects to be ordered based on f value
    def __lt__(self, other):
        return self.f < other.f

# Heuristic function (Manhattan distance) for A* search
def heuristic(a, b):
    """Manhattan distance between two points."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* search algorithm to find the shortest path on the grid
def a_star_search(grid, start, goal):
    open_list = []  # List of nodes to be evaluated (priority queue)
    closed_set = set()  # Set of nodes already evaluated
    start_node = Node(start)  # Create the start node
    heapq.heappush(open_list, start_node)  # Add the start node to the open list

    while open_list:
        # Get the node with the lowest f value (best candidate)
        current_node = heapq.heappop(open_list)

        # If the current node is the goal, reconstruct the path
        if current_node.position == goal:
            path = []
            while current_node:
                path.append(current_node.position)  # Add the current node to the path
                current_node = current_node.parent  # Move to the parent node
            return path[::-1]  # Return the reversed path (from start to goal)

        closed_set.add(current_node.position)  # Mark the current node as evaluated
        x, y = current_node.position  # Current position

        # Check all possible neighbors (left, right, up, down)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor_pos = (x + dx, y + dy)

            # Check if the neighbor is within bounds and not a wall (0 = open path)
            if (0 <= neighbor_pos[0] < len(grid) and
                0 <= neighbor_pos[1] < len(grid[0]) and
                grid[neighbor_pos[0]][neighbor_pos[1]] == 0 and
                neighbor_pos not in closed_set):
                
                # Create a new node for the neighbor
                neighbor = Node(neighbor_pos, current_node)
                neighbor.g = current_node.g + 1  # Update the g value (cost from start)
                neighbor.h = heuristic(neighbor_pos, goal)  # Update the h value (heuristic)
                neighbor.f = neighbor.g + neighbor.h  # Update the f value (total cost)

                # If a node with the same position and a lower f value is in the open list, skip it
                if any(open_node.position == neighbor.position and open_node.f <= neighbor.f for open_node in open_list):
                    continue

                # Add the neighbor node to the open list
                heapq.heappush(open_list, neighbor)

    return None  # If no path is found, return None

# Function to print the grid with the path marked
def print_grid_with_path(grid, path):
    # Create a visual grid where ' ' represents an empty space, and '#' represents a wall
    visual_grid = [[' ' if cell == 0 else '#' for cell in row] for row in grid]

    # Mark the path with '*' characters
    for x, y in path:
        visual_grid[x][y] = '*'

    # Mark the start and goal positions with 'S' and 'G'
    sx, sy = path[0]
    gx, gy = path[-1]
    visual_grid[sx][sy] = 'S'
    visual_grid[gx][gy] = 'G'

    # Print the visual grid
    print("\nGrid with path:")
    for row in visual_grid:
        print(' '.join(row))

# Example grid where 0 represents an open path and 1 represents a wall
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)  # Starting position
goal = (4, 4)   # Goal position

# Run the A* search algorithm
path = a_star_search(grid, start, goal)

# Show the result
if path:
    print("Path found:")
    print(path)  # Print the path from start to goal
    print_grid_with_path(grid, path)  # Display the grid with the path marked
else:
    print("No path found.")  # If no path is found, print this message



# Path found:
# [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]

# Grid with path:
# S # * * *
# * # * # *
# * * * # *
# # # * # *
# * * * * G
