import random
from dataclasses import dataclass
import numpy as np
import torch
import torch.nn as nn

class QNet(nn.Module):
    def __init__(self,state_dim=32,action_dim=3): super().__init__(); self.net=nn.Sequential(nn.Linear(state_dim,64),nn.ReLU(),nn.Linear(64,64),nn.ReLU(),nn.Linear(64,action_dim))
    def forward(self,x): return self.net(x)
@dataclass
class Transition: state:np.ndarray; action:int; reward:float; next_state:np.ndarray; done:bool
class MultiAgentDQN:
    def __init__(self,state_dim=32,action_dim=3,lr=5e-4):
        self.q=QNet(state_dim,action_dim); self.target=QNet(state_dim,action_dim); self.target.load_state_dict(self.q.state_dict()); self.opt=torch.optim.Adam(self.q.parameters(),lr=lr); self.memory=[]
    def select(self,state,epsilon=.1):
        if random.random()<epsilon: return random.randrange(3)
        with torch.no_grad(): return int(self.q(torch.tensor(state,dtype=torch.float32)).argmax())
    def update(self,batch,gamma=.99):
        s=torch.tensor(np.asarray([b.state for b in batch]),dtype=torch.float32); a=torch.tensor([b.action for b in batch]); r=torch.tensor([b.reward for b in batch],dtype=torch.float32); ns=torch.tensor(np.asarray([b.next_state for b in batch]),dtype=torch.float32); d=torch.tensor([b.done for b in batch],dtype=torch.float32)
        q=self.q(s).gather(1,a[:,None]).squeeze(1); target=r+gamma*(1-d)*self.target(ns).max(1).values.detach(); loss=((q-target)**2).mean(); self.opt.zero_grad(); loss.backward(); self.opt.step(); return float(loss.detach())
