from collections import deque

def bfs(graph, start):
    visited=set() # Tracks visited nodes to avoid cycles
    q=deque([start]) # Queue for BFS traversal
    res=[] # Stores the order of visited nodes

    while q:
        node = q.popleft()
        visited.add(node)
        res.append(node) 
        for neighbour in graph[node]:
            if neighbour not in visited:
                q.append(neighbour)
                visited.add(neighbour)

    return res

def main():
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D'],
        'D': ['B', 'C', 'E'],
        'E': ['D'],
    }

    print(bfs(graph, 'A'))

if __name__ == '__main__':
    main()