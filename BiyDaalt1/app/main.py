from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .schemas import RouteRequest, RouteResponse
from .graph import load_graph
from .geo import to_latlon, nearest_node, path_length_m
from .algorithms.bfs import bfs_path
from .algorithms.dfs import dfs_path
from .algorithms.dijkstra import dijkstra_path

app = FastAPI(title="UB Routing API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

G = load_graph()

@app.get("/health")
def health():
    return {"ok": True, "nodes": len(G)}

@app.post("/route", response_model=RouteResponse)
def route(req: RouteRequest):
    s = nearest_node(G, req.start) 
    t = nearest_node(G, req.goal)

    if s is None or t is None:
        raise HTTPException(status_code=400, detail="Nearest nodes not found.")

    if req.algo == "bfs":
        path = bfs_path(G, s, t)   
        total_m = path_length_m(G, path)
    elif req.algo == "dfs":
        path = dfs_path(G, s, t)
        total_m = path_length_m(G, path)
    elif req.algo == "dijkstra":
        path, total_m = dijkstra_path(G, s, t)
    else:
        raise HTTPException(status_code=400, detail="Unknown algorithm")

    if not path:
        raise HTTPException(status_code=404, detail="No path found")

    path_latlon = [to_latlon(n) for n in path]

    stats = {
        "length_m": float(total_m),
        "steps": max(0, len(path) - 1),
    }
    return RouteResponse(path=path_latlon, stats=stats)
