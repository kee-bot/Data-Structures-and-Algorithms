"""Dijkstra's algorithm demo (self-contained).

This file implements Dijkstra's shortest-path algorithm without importing
anything from other project files. It operates on a simple adjacency
representation: a dict mapping node -> list of (neighbour, weight) pairs.
"""
from heapq import heappush, heappop
from typing import Dict, Tuple, List, Optional


def dijkstra(adj: Dict[str, List[Tuple[str, float]]], source: str) -> Tuple[Dict[str, float], Dict[str, Optional[str]]]:
    """Compute shortest path distances from source using a min-heap.

    adj: adjacency mapping node -> list of (neighbour, weight)
    Returns (dist, prev) where prev[node] is the predecessor on the shortest path.
    """
    # initialize distances and predecessors
    dist: Dict[str, float] = {n: float('inf') for n in adj.keys()}
    prev: Dict[str, Optional[str]] = {n: None for n in adj.keys()}

    if source not in adj:
        raise KeyError(f"Source node {source!r} not in graph")

    dist[source] = 0.0
    heap: List[Tuple[float, str]] = [(0.0, source)]

    while heap:
        d, u = heappop(heap)
        if d > dist[u]:
            continue

        for v, w in adj.get(u, []):
            # ensure weight is float
            weight = float(w)
            alt = d + weight
            if alt < dist.get(v, float('inf')):
                dist[v] = alt
                prev[v] = u
                heappush(heap, (alt, v))

    return dist, prev


def reconstruct_path(prev: Dict[str, Optional[str]], target: str) -> List[str]:
    """Reconstruct path from predecessor map; returns list of nodes (may be just [target])."""
    path: List[str] = []
    cur = target
    while cur is not None:
        path.append(cur)
        cur = prev.get(cur)
    return list(reversed(path))


def build_adj_from_edges(edges: List[Tuple[str, str, float]], directed: bool = True) -> Dict[str, List[Tuple[str, float]]]:
    adj: Dict[str, List[Tuple[str, float]]] = {}
    def ensure(n: str):
        if n not in adj:
            adj[n] = []

    for u, v, w in edges:
        ensure(u); ensure(v)
        adj[u].append((v, float(w)))
        if not directed:
            adj[v].append((u, float(w)))

    return adj


def demo():
    # Example directed weighted graph
    edges = [
        ('A', 'B', 1),
        ('A', 'C', 4),
        ('B', 'C', 2),
        ('B', 'D', 5),
        ('C', 'D', 1),
        ('D', 'E', 3),
    ]

    adj = build_adj_from_edges(edges, directed=True)

    print('Adjacency list:')
    for u in sorted(adj.keys()):
        print(f"  {u} -> {adj[u]}")

    source = 'A'
    dist, prev = dijkstra(adj, source)

    print('\nDistances from', source)
    for n in sorted(dist.keys()):
        d = dist[n]
        print(f"  {n}: {d if d != float('inf') else 'inf'}")

    # show shortest path A -> E
    target = 'E'
    if dist.get(target, float('inf')) == float('inf'):
        print(f"{target} is unreachable from {source}")
    else:
        path = reconstruct_path(prev, target)
        print(f"Shortest path {source} -> {target}: {path} (cost {dist[target]})")


if __name__ == '__main__':
    demo()
