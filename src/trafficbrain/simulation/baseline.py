from .types import SignalAction

class FixedTimeController:
    def __init__(self,env,cycle=30): self.env=env; self.cycle=cycle; self.t=0
    def act(self,obs):
        self.t+=1; delta=1 if self.t%self.cycle<self.cycle//2 else -1
        return [SignalAction(j,delta) for j in range(self.env.junctions)]

class PressureController:
    def __init__(self,env): self.env=env
    def act(self,obs):
        q=obs["queues"]
        return [SignalAction(j,1 if q[j,0]+q[j,2]>=q[j,1]+q[j,3] else -1) for j in range(self.env.junctions)]
