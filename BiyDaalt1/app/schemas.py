from typing import Literal, List, Tuple, Dict
from pydantic import BaseModel, Field

Algo = Literal["bfs", "dfs", "dijkstra"]

class RouteRequest(BaseModel):
    start: Tuple[float, float] = Field(..., description="(lat, lon)")
    goal:  Tuple[float, float] = Field(..., description="(lat, lon)")
    algo:  Algo = "dijkstra"

class RouteResponse(BaseModel):
    path: List[Tuple[float, float]]
    stats: Dict[str, float]
