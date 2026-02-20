def dfs(graph, start):
    visited=set() # Tracks visited nodes to avoid cycles
    stk=[start] # Stack for DFS traversal
    res=[] # Stores the order of visited nodes

    while stk:
        node = stk.pop()
        visited.add(node)
        res.append(node) 
        for neighbour in graph[node]:
            if neighbour not in visited:
                stk.append(neighbour)
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

    print(dfs(graph, 'A'))

if __name__ == '__main__':
    main()