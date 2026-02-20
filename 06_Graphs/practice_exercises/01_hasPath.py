# Problem: Given a acyclic directed graph, determine if there is a path between two nodes.

# Solution: We can use either DFS or BFS to check if there is a path between the two nodes. We will implement both iterative and recursive versions of the DFS approach.

def has_path(graph, start, end):
    """Iterative DFS to check reachability from start to end.
    """
    if start == end:
        return True

    visited = set()
    stk = [start]  # explicit stack for DFS

    while stk:
        node = stk.pop()
        # found the target
        if node == end:
            return True
        if node in visited:
            continue
        visited.add(node)
        # push neighbours to the stack; neighbours not yet visited will be explored
        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                stk.append(neighbour)

    return False

def recursive_has_path(graph, start, end, visited):
    """Recursive DFS for reachability.
    """
    if start == end:
        return True
    
    if start in visited:
        return False

    for neighbour in graph.get(start, []):
        # recursively search each neighbour
        if recursive_has_path(graph, neighbour, end, visited):
            return True
    return False
        
def main():
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': ['E'],
        'E': [],
    }

    print(has_path(graph, 'A', 'E'))  # True
    print(recursive_has_path(graph, 'A', 'E',set()))

    # Additional case: directed graph where start and end exist but no path
    dir_graph = {
        'A': ['B'],
        'B': [],
        'C': ['A'],
    }

    # B -> A does not exist (A->B exists but not the reverse)
    print(has_path(dir_graph, 'B', 'A'))  # False
    print(recursive_has_path(graph, 'B', 'A',set()))

    # Test with a cycle
    cyclic_graph = {
        'A': ['B'],
        'B': ['C'],
        'C': ['A'],  # cycle A -> B -> C -> A
    }

    print(has_path(cyclic_graph, 'A', 'A'))  # True (self-loop)
    print(recursive_has_path(cyclic_graph, 'A', 'A',set()))  # True (self-loop)

if __name__ == '__main__':
    main()