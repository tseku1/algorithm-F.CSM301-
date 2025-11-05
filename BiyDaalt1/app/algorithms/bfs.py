from collections import deque
from typing import Dict, Tuple, List

Node = Tuple[float, float]
Graph = Dict[Node, Dict[Node, float]]

def bfs_path(G: Graph, start: Node, goal: Node) -> List[Node]:
    if start == goal:
        return [start]
    q = deque([start])
    seen = {start}
    parent = {start: None}

    while q:
        u = q.popleft()
        for v in G.get(u, {}):
            if v not in seen:
                seen.add(v)
                parent[v] = u
                if v == goal:
                    path = [v]
                    while path[-1] is not None:
                        prev = parent[path[-1]]
                        if prev is None:
                            break
                        path.append(prev)
                    path.append(start)
                    path.reverse()
                    return path
                q.append(v)
    return []
