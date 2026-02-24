# Problem: Given a graph without weights, find the shortest path (in terms of number of edges) between two nodes.

"""
Shortest path for an unweighted graph is similar to BFS. 
"""

from collections import deque

# Finds shortest path between start and end nodes. Returns the path as a list of nodes.
def shortest_path(graph, start, end):
    if start == end:
        return [start]
    visited = set([start])
    q = deque([start])
    parent = {start: None}

    while q:
        node = q.popleft()
        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                visited.add(neighbour)
                parent[neighbour] = node
                if neighbour == end:
                    # Reconstruct path
                    path = [end]
                    while node is not None:
                        path.append(node)
                        node = parent[node]
                    return path[::-1]
                q.append(neighbour)
    return "No path found"

# Finds the length of the shortest path between start and end nodes. Returns the length as an integer.
def shortest_path_length(graph, start, end):
    if start == end:
        return 0
    visited = set([start])
    q = deque([(start, 0)])
    while q:
        node, dist = q.popleft()
        if node == end:
            return dist
        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                visited.add(neighbour)
                q.append((neighbour, dist + 1))
    return -1

def main():
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D'],
        'D': ['B', 'C', 'E'],
        'E': ['D'],
    }

    print(shortest_path(graph, 'A','C'))
    print(shortest_path_length(graph, 'A','C'))

if __name__ == '__main__':
    main()