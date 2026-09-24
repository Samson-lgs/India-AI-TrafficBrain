class SumoAdapter:
    """Explicit future integration boundary for SUMO/TraCI."""
    def __init__(self,command=None): self.command=command
    def available(self): return False
