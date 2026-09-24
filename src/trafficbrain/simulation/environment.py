from __future__ import annotations
import random
import numpy as np

class TrafficNetwork:
    def __init__(self, seed=7, junctions=6, approaches=4):
        self.rng=random.Random(seed)
        self.junctions=junctions; self.approaches=approaches
        self.queues=np.zeros((junctions,approaches),dtype=float)
        self.speeds=np.ones((junctions,approaches))*25
        self.signal=np.zeros(junctions,dtype=int); self.time=0
    def reset(self):
        self.queues.fill(0); self.signal.fill(0); self.time=0; return self.observe()
    def observe(self):
        return {"queues":self.queues.copy(),"speeds":self.speeds.copy(),"waiting_seconds":(self.queues/2).sum(axis=1).tolist(),"signal":self.signal.copy(),"time":self.time}
    def step(self, actions):
        for j in range(self.junctions):
            arrivals=np.array([self.rng.uniform(.5,2.5) for _ in range(self.approaches)])
            self.queues[j]+=arrivals
            if self.signal[j]==0: service=np.array([1.2,.8,1.2,.8])
            else: service=np.array([.8,1.2,.8,1.2])
            self.queues[j]=np.maximum(0,self.queues[j]-np.minimum(self.queues[j],service))
        for a in actions if isinstance(actions,list) else []:
            self.signal[a.junction_id]=0 if a.delta_green>=0 else 1
        self.time+=1; return self.observe()
    def total_vehicles(self): return int(self.queues.sum())
