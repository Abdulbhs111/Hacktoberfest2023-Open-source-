import sys

# Define a function to find the shortest paths using Floyd-Warshall algorithm
def floyd_warshall(graph):
    V = len(graph)
    dist = [[float('inf')] * V for _ in range(V)]

    for i in range(V):
        dist[i][i] = 0

    for u in range(V):
        for v in range(V):
            dist[u][v] = graph[u][v]

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

# Example usage
# Create an adjacency matrix for a weighted directed graph
graph = [
    [0, 3, float('inf'), 2],
    [float('inf'), 0, 2, float('inf')],
    [float('inf'), float('inf'), 0, 4],
    [float('inf'), 1, float('inf'), 0]
]

shortest_paths = floyd_warshall(graph)

# Print the shortest path distances
for i in range(len(shortest_paths)):
    for j in range(len(shortest_paths[i])):
        if shortest_paths[i][j] == float('inf'):
            print("INF", end="\t")
        else:
            print(shortest_paths[i][j], end="\t")
    print()
