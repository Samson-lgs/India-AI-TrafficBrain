from dataclasses import dataclass

@dataclass
class Junction:
    junction_id:int
    queue_by_approach:list[float]

@dataclass
class TrafficGraph:
    adjacency:list[list[float]]
