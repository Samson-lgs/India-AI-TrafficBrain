from dataclasses import dataclass
from .metrics import compute_metrics
@dataclass
class BenchmarkResult: controller:str; metrics:dict
def benchmark(controller_name,history): return BenchmarkResult(controller_name,compute_metrics(history))
