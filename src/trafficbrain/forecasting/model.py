import torch
import torch.nn as nn
from .graph import normalize_adjacency
from .dataset import synthetic_graph_batch

class TemporalGraphForecaster(nn.Module):
    def __init__(self,features=4,hidden=32,horizon=6):
        super().__init__(); self.gcn=nn.Linear(features,hidden); self.temporal=nn.Conv1d(hidden,hidden,3,padding=1); self.head=nn.Linear(hidden,horizon)
    def forward(self,x,adj):
        a=normalize_adjacency(adj); h=torch.relu(self.gcn(x[:,-1])); h=torch.relu(a.unsqueeze(0)@h); h=self.temporal(h.transpose(1,2)).transpose(1,2); return self.head(h).transpose(1,2).unsqueeze(-1)

def run_smoke_forecaster(epochs=2):
    model=TemporalGraphForecaster(); opt=torch.optim.Adam(model.parameters(),lr=1e-3); x,y,a=synthetic_graph_batch()
    for _ in range(epochs):
        pred=model(x,a); loss=((pred-y)**2).mean(); opt.zero_grad(); loss.backward(); opt.step()
    print({'forecast_smoke_mse':float(loss.detach())})
