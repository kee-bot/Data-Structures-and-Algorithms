from collections import deque

class Graph:
    """Adjacency-list graph where neighbours are stored as (node, weight) tuples.

    We normalize internal storage so every neighbour is a tuple (node, weight),
    with weight=None for unweighted edges. This simplifies traversal and
    edge operations.
    """

    def __init__(self, directed=False):
        self.directed = directed
        # dict[node] -> set of (neighbour, weight) tuples
        self.adj_list = {}

    def __repr__(self):
        parts = []
        for node in sorted(self.adj_list.keys()):
            neigh = sorted(
                self.adj_list[node], key=lambda x: (x[0], x[1] if x[1] is not None else -float('inf'))
            )
            repr_neigh = [f"{n}" if w is None else f"{n}({w})" for n, w in neigh]
            parts.append(f"{node} -> [{', '.join(repr_neigh)}]")
        return f"Graph(directed={self.directed})\n" + "\n".join(parts)

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = set()
        else:
            raise ValueError("Node exists already")

    def remove_node(self, node):
        if node not in self.adj_list:
            raise ValueError("Node does not exist")

        # remove any references to `node` from neighbour sets
        for neighbours in self.adj_list.values():
            to_remove = {n for n in neighbours if n[0] == node}
            for r in to_remove:
                neighbours.discard(r)

        del self.adj_list[node]

    def add_edge(self, from_node, to_node, weight=None):
        # ensure nodes exist
        if from_node not in self.adj_list:
            self.add_node(from_node)
        if to_node not in self.adj_list:
            self.add_node(to_node)

        self.adj_list[from_node].add((to_node, weight))
        if not self.directed:
            self.adj_list[to_node].add((from_node, weight))

    def remove(self, from_node, to_node):
        # remove edge from from_node -> to_node (any weight)
        if from_node not in self.adj_list:
            raise ValueError("Edge does not exist")

        # find tuple(s) to remove
        to_remove = {n for n in self.adj_list[from_node] if n[0] == to_node}
        if not to_remove:
            raise ValueError("Edge does not exist")

        for r in to_remove:
            self.adj_list[from_node].remove(r)

        if not self.directed:
            # remove reverse edge(s)
            rev_remove = {n for n in self.adj_list.get(to_node, set()) if n[0] == from_node}
            for r in rev_remove:
                self.adj_list[to_node].remove(r)

    def get_neighbours(self, node):
        # returns set of (node, weight) tuples
        return self.adj_list.get(node, set())

    def has_node(self, node):
        return node in self.adj_list

    def has_edge(self, from_node, to_node):
        neighbours = self.adj_list.get(from_node)
        if not neighbours:
            return False
        return any(n == to_node for n, _ in neighbours)

    def get_node(self):
        # keep legacy name
        return list(self.adj_list.keys())

    def get_nodes(self):
        return list(self.adj_list.keys())

    def get_edges(self):
        # return list of (from, to, weight) tuples (weight may be None)
        edges = []
        for u, neighbours in self.adj_list.items():
            for v, w in neighbours:
                edges.append((u, v, w))
        return edges

    def bfs(self, start):
        if start not in self.adj_list:
            return []

        visited = {start}
        q = deque([start])
        order = []

        while q:
            node = q.popleft()
            order.append(node)
            # deterministic neighbor order
            next_nodes = sorted(n for n, _ in self.get_neighbours(node))
            for neighbour in next_nodes:
                if neighbour not in visited:
                    visited.add(neighbour)
                    q.append(neighbour)

        return order

    def dfs(self, start):
        if start not in self.adj_list:
            return []

        visited = {start}
        stack = [start]
        order = []

        while stack:
            node = stack.pop()
            order.append(node)
            # deterministic neighbor order; push in reverse so smallest visited first
            next_nodes = sorted(n for n, _ in self.get_neighbours(node))
            for neighbour in reversed(next_nodes):
                if neighbour not in visited:
                    visited.add(neighbour)
                    stack.append(neighbour)

        return order
                    
def main():
    #Create an undirected graph with a weighted edge and run basic operations
    g = Graph(directed=False)
    g.add_node('A')
    g.add_node('B')
    g.add_edge('A', 'B')
    g.add_node('C')
    g.add_edge('A', 'C')
    g.add_edge('C','W', weight=5)
    print(repr(g))

    print(g.get_edges())
    print(g.get_node())
    print(g.get_neighbours('A'))

    print(g.bfs('A'))
    print(g.dfs('A'))

    #Create a directed graph with a weighted edge and run basic operations
    dg = Graph(directed=True)
    # create a simple chain A -> B -> C and a weighted edge C -> W
    dg.add_edge('A', 'B')
    dg.add_edge('B', 'C')
    dg.add_edge('C', 'W', weight=7)

    print(repr(dg))
    print('edges:', dg.get_edges())
    print('nodes:', dg.get_nodes())
    print("neighbours of A:", dg.get_neighbours('A'))
    # show directionality
    print('A->B?', dg.has_edge('A', 'B'))
    print('B->A?', dg.has_edge('B', 'A'))

    print('BFS from A:', dg.bfs('A'))
    print('DFS from A:', dg.dfs('A'))

    
if __name__=="__main__":
    main()

                
                



























