# Dijkstra's Algorithm (Greedy Search for Shortest Path)
import heapq  # Import heapq for implementing a priority queue (min-heap)

def dijkstra(graph, start):
    # Priority queue: (distance, node)
    queue = [(0, start)]  # Start with the source node 'start' and distance 0
    distances = {node: float('inf') for node in graph}  # Set initial distances to infinity for all nodes
    distances[start] = 0  # Distance to start node is 0
    visited = set()  # Set to track visited nodes

    while queue:
        # Pop the node with the smallest distance from the priority queue
        current_distance, current_node = heapq.heappop(queue)
        print(f"Visiting node {current_node} with current distance {current_distance}")  # Debugging line

        # If the node has already been visited, skip it
        if current_node in visited:
            continue
        visited.add(current_node)  # Mark the current node as visited

        # Loop through all the neighbors of the current node
        for neighbor, weight in graph[current_node]:
            # Calculate the distance to the neighbor via the current node
            distance = current_distance + weight
            print(f"Checking neighbor {neighbor} with edge weight {weight}")  # Debugging line

            # If a shorter path to the neighbor is found, update its distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))  # Add the neighbor to the priority queue
                print(f"Updated distance for {neighbor}: {distance}")  # Debugging line

    return distances  # Return the final shortest distances to all nodes

# Example Graph (Adjacency list representation)
graph = {
    'A': [('B', 4), ('C', 2)],  # Node A connects to B with weight 4, and C with weight 2
    'B': [('A', 4), ('C', 1), ('D', 5)],  # Node B connects to A (4), C (1), and D (5)
    'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],  # Node C connects to A (2), B (1), D (8), and E (10)
    'D': [('B', 5), ('C', 8), ('E', 2), ('Z', 6)],  # Node D connects to B (5), C (8), E (2), and Z (6)
    'E': [('C', 10), ('D', 2), ('Z', 3)],  # Node E connects to C (10), D (2), and Z (3)
    'Z': [('D', 6), ('E', 3)]  # Node Z connects to D (6) and E (3)
}

# Run Dijkstra from the start node 'A'
start_node = 'A'
shortest_paths = dijkstra(graph, start_node)

# Print the results: shortest distances from the start node to all other nodes
print(f"Shortest distances from node {start_node}:")
for node, dist in shortest_paths.items():
    print(f"To {node}: {dist}")



# Visiting node A with current distance 0
# Checking neighbor B with edge weight 4
# Updated distance for B: 4
# Checking neighbor C with edge weight 2
# Updated distance for C: 2
# Visiting node C with current distance 2
# Checking neighbor A with edge weight 2
# Checking neighbor B with edge weight 1
# Updated distance for B: 3
# Checking neighbor D with edge weight 8
# Updated distance for D: 10
# Checking neighbor E with edge weight 10
# Updated distance for E: 12
# Visiting node B with current distance 3
# Checking neighbor A with edge weight 4
# Checking neighbor C with edge weight 1
# Checking neighbor D with edge weight 5
# Updated distance for D: 8
# Visiting node D with current distance 8
# Checking neighbor B with edge weight 5
# Checking neighbor C with edge weight 8
# Checking neighbor E with edge weight 2
# Updated distance for E: 10
# Checking neighbor Z with edge weight 6
# Updated distance for Z: 14
# Visiting node E with current distance 10
# Checking neighbor C with edge weight 10
# Checking neighbor D with edge weight 2
# Checking neighbor Z with edge weight 3
# Updated distance for Z: 13
# Visiting node Z with current distance 13
# Checking neighbor D with edge weight 6
# Checking neighbor E with edge weight 3
# Shortest distances from node A:
# To A: 0
# To B: 3
# To C: 2
# To D: 8
# To E: 10
# To Z: 13
