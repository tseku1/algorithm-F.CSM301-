import geopandas as gpd
from shapely.geometry import LineString, box
from typing import Dict, Tuple
from .geo import haversine_m

Node = Tuple[float, float]  # (lon, lat)
Graph = Dict[Node, Dict[Node, float]]

UB_BBOX = box(106.81, 47.88, 107.01, 47.96)

def _add_edge(G: Graph, u: Node, v: Node, w: float):
    if u == v:
        return
    if u not in G:
        G[u] = {}
    if v not in G:
        G[v] = {}
    G[u][v] = w
    G[v][u] = w

def load_graph() -> Graph:
    try:
        gdf = gpd.read_file("mongolia-251028-free.shp", layer="gis_osm_roads_free_1")
    except Exception:
        gdf = gpd.read_file("mongolia-251028-free.shp/gis_osm_roads_free_1.shp")

    gdf = gdf[gdf.intersects(UB_BBOX)].reset_index(drop=True)

    G: Graph = {}
    for geom in gdf.geometry:
        if isinstance(geom, LineString):
            coords = list(geom.coords)
            for i in range(len(coords) - 1):
                u = (float(coords[i][0]),   float(coords[i][1]))
                v = (float(coords[i+1][0]), float(coords[i+1][1]))
                w = haversine_m(u, v)
                _add_edge(G, u, v, w)
    return G
