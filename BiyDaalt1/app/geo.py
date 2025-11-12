import math
from typing import Tuple, Dict, List
# уртраг, өргөрөгийг тодорхойлно
Node = Tuple[float, float]

def haversine_m(a: Node, b: Node) -> float:
    lon1, lat1 = a
    lon2, lat2 = b
    # Дэлхийн дундаж радиус
    R = 6371000.0
    # бүх өнцгийг тодорхойлно
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlbd = math.radians(lon2 - lon1)
    # Бүх өнцгийг радиан руу хөрвүүлээд Haversine томьёо
    s = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlbd/2)**2
    return 2 * R * math.asin(math.sqrt(s))

def nearest_node(G: Dict[Node, Dict[Node, float]], latlon: Tuple[float, float]) -> Node:
    lat, lon = latlon
    target = (lon, lat)
    
    best = None
    best_d2 = None

    for n in G.keys():
        dx = n[0] - target[0]
        dy = n[1] - target[1]
        d2 = dx*dx + dy*dy

        if best is None or d2 < best_d2:
            best, best_d2 = n, d2
    
    return best

def to_latlon(node: Node) -> Tuple[float, float]:

    return (node[1], node[0])

def path_length_m(G: Dict[Node, Dict[Node, float]], path: List[Node]) -> float:

    total = 0.0
    
    for u, v in zip(path[:-1], path[1:]):
        if v in G.get(u, {}):
            total += G[u][v]
        else:
            print(f"Warning: No connection between {u} and {v}")
            continue 

    return total  
