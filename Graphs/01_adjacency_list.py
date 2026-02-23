from collections import defaultdict
from typing import Dict, List, Any

class Graph:
    """
    Simple adjacency list graph implementation.

    Supports:
    - Directed or undirected graphs
    - Adding vertices
    - Adding edges
    - Getting neighbors
    """

    def __init__(self, directed: bool = False):
        self.directed = directed
        self.adj: Dict[Any, List[Any]] = defaultdict(list)

    def add_vertex(self, vertex: Any) -> None:
        """Add a vertex to the graph."""
        if vertex not in self.adj:
            self.adj[vertex] = []

    def add_edge(self, u: Any, v: Any) -> None:
        """Add an edge from u to v."""
        self.adj[u].append(v)
        if not self.directed:
            self.adj[v].append(u)

    def neighbors(self, vertex: Any) -> List[Any]:
        """Return neighbors of a vertex."""
        return self.adj[vertex]

    def vertices(self) -> List[Any]:
        """Return all vertices in the graph."""
        return list(self.adj.keys())

    def __repr__(self) -> str:
        return f"Graph(directed={self.directed}, adj={dict(self.adj)})"
    
def main():
    g = Graph(directed=False)

    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")

    print(g.adj)

if __name__ == "__main__":
    main()
