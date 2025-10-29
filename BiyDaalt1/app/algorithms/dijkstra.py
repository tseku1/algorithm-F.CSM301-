import heapq
from typing import Dict, Tuple, List

Node = Tuple[float, float]
Graph = Dict[Node, Dict[Node, float]]

def dijkstra_path(G: Graph, start: Node, goal: Node):
    if start == goal:
        return [start], 0.0

    pq = [(0.0, start)]
    dist = {start: 0.0}
    parent = {start: None}
    seen = set()

    while pq:
        d, u = heapq.heappop(pq)
        if u in seen:
            continue
        seen.add(u)

        if u == goal:
            break

        for v, w in G.get(u, {}).items():
            nd = d + w
            if nd < dist.get(v, float("inf")):
                dist[v] = nd
                parent[v] = u
                heapq.heappush(pq, (nd, v))

    if goal not in parent:
        return [], 0.0

    path = [goal]
    while path[-1] is not None:
        prev = parent[path[-1]]
        if prev is None:
            break
        path.append(prev)
    path.append(start)
    path.reverse()
    return path, dist.get(goal, 0.0)
