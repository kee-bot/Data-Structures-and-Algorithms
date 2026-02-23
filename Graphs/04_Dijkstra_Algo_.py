import heapq

def dijkstra_with_path(graph, start):
    """
    graph: dict[node] = list of (neighbor, weight)
    start: starting node
    
    Returns:
        distances: dict of shortest distances
        shortest_path: function(target) -> list representing path
    """

    heap = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # To reconstruct path
    previous = {}

    while heap:
        current_dist, node = heapq.heappop(heap)

        if current_dist > distances[node]:
            continue

        for neighbor, weight in graph[node]:
            new_dist = current_dist + weight

            if new_dist < distances.get(neighbor, float('inf')):
                distances[neighbor] = new_dist
                previous[neighbor] = node
                heapq.heappush(heap, (new_dist, neighbor))

    def shortest_path(target):
        """Reconstruct shortest path from start to target."""
        if distances.get(target, float('inf')) == float('inf'):
            return None  # No path exists

        path = []
        current = target

        while current != start:
            path.append(current)
            current = previous[current]

        path.append(start)
        path.reverse()
        return path

    return distances, shortest_path

def main():
    graph = {
        "A": [("B", 1), ("C", 4)],
        "B": [("C", 2), ("D", 5)],
        "C": [("D", 1)],
        "D": []
    }

    distances, shortest_path = dijkstra_with_path(graph, "A")

    print(distances)
    # {'A': 0, 'B': 1, 'C': 3, 'D': 4}

    print(shortest_path("D"))
    # ['A', 'B', 'C', 'D']

if __name__ == "__main__":
    main()