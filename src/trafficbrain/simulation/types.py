from dataclasses import dataclass

@dataclass
class SignalAction:
    junction_id: int
    delta_green: int = 0

@dataclass
class Vehicle:
    kind: str
    speed_kph: float = 0.0
    wait_s: float = 0.0
