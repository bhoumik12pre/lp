# Importing deque from collections for efficient queue operations in BFS
from collections import deque

# Function to perform Depth-First Search (DFS)
def dfs(visited, graph, node):
    # If the node hasn't been visited yet
    if node not in visited:
        # Print the current node (part of the DFS traversal)
        print(node, end=" ")
        # Mark the node as visited
        visited.add(node)
        # Visit all the neighbors of the current node recursively
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Function to perform Breadth-First Search (BFS)
def bfs(visited, graph, start_node, queue):
    # Mark the start node as visited and enqueue it
    visited.add(start_node)
    queue.append(start_node)

    # While there are nodes in the queue, continue with BFS
    while queue:
        # Dequeue the next node
        current = queue.popleft()
        # Print the current node (part of the BFS traversal)
        print(current, end=" ")
        # Visit each neighbor of the current node
        for neighbour in graph[current]:
            # If the neighbor hasn't been visited yet
            if neighbour not in visited:
                # Mark the neighbor as visited and enqueue it
                visited.add(neighbour)
                queue.append(neighbour)

# Main function to drive the program
def main():
    # Sets to track visited nodes for DFS and BFS
    visited_dfs = set()  # For DFS
    visited_bfs = set()  # For BFS
    queue = deque()      # Deque to efficiently manage BFS queue
    graph = dict()       # Dictionary to represent the graph

    # Input: Number of nodes in the graph
    n = int(input("Enter number of nodes: "))
    
    # Initialize the graph with empty adjacency lists for each node
    for i in range(1, n + 1):
        graph[i] = []

    # Input: Define edges for each node to build the graph
    for i in range(1, n + 1):
        edges = int(input(f"Enter number of edges for node {i}: "))
        for j in range(1, edges + 1):
            node = int(input(f"Enter edge {j} for node {i}: "))
            # Add the node to the adjacency list of node i
            graph[i].append(node)
            # Add the reverse edge to make the graph undirected
            if node in graph:
                graph[node].append(i)
            else:
                graph[node] = [i]

    # Input: Starting node for traversal
    start = int(input("Enter the starting node for traversal: "))
    
    # Check if the starting node is valid in the graph
    if start not in graph:
        print("Invalid starting node.")
        return

    # Perform DFS traversal starting from the chosen node
    print("The following is DFS:")
    dfs(visited_dfs, graph, start)

    # Print a newline for separation
    print("\nThe following is BFS:")
    # Perform BFS traversal starting from the chosen node
    bfs(visited_bfs, graph, start, queue)

# This ensures that the program starts executing from the main function when run
if __name__ == "__main__":
    main()





# Enter number of nodes: 4
# Enter number of edges for node 1: 2
# Enter edge 1 for node 1: 2
# Enter edge 2 for node 1: 3
# Enter number of edges for node 2: 1
# Enter edge 1 for node 2: 4
# Enter number of edges for node 3: 0
# Enter number of edges for node 4: 0
# Enter the starting node for traversal: 1


# Enter number of nodes: 7
# Enter number of edges for node 1: 2
# Enter edge 1 for node 1: 2
# Enter edge 2 for node 1: 3
# Enter number of edges for node 2: 2
# Enter edge 1 for node 2: 4
# Enter edge 2 for node 2: 5
# Enter number of edges for node 3: 2
# Enter edge 1 for node 3: 6
# Enter edge 2 for node 3: 7
# Enter number of edges for node 4: 0
# Enter number of edges for node 5: 0
# Enter number of edges for node 6: 0
# Enter number of edges for node 7: 0
# Enter the starting node for traversal: 1