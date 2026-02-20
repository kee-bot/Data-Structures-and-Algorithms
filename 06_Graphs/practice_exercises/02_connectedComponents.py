# Problem: Given an undirected graph, find all connected components.

def dfs(graph, start,visited):
    stk=[start] # Stack for DFS traversal
    while stk:
        node = stk.pop()
        visited.add(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                stk.append(neighbour)
                visited.add(neighbour)

def component_count(graph): 
    visited=set()
    ct=0

    for val in graph.keys():
        if val not in visited: 
            dfs(graph,val,visited)
            ct+=1

    return(ct)        

def main():
    graph = {
        0: [8, 1, 5],
        1: [0],
        5: [0, 8],
        8: [0, 5],
        2: [3, 4],
        3: [2, 4],
        4: [3, 2]
        }

    print(component_count(graph)) # Output: 2

    graph = {
        0: [4,7],
        1: [],
        2: [],
        3: [6],
        4: [0],
        6: [3],
        7: [0],
        8: []
        }

    print(component_count(graph)) # Output: 5

    graph = {
        3: [],
        4: [6],
        6: [4, 5, 7, 8],
        8: [6],
        7: [6],
        5: [6],
        1: [2],
        2: [1]
        }

    print(component_count(graph)) # Output: 3

if __name__ == '__main__':
    main()