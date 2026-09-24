import torch

def normalize_adjacency(adj):
    a=adj+torch.eye(adj.shape[0],device=adj.device); d=a.sum(-1); inv=torch.diag(torch.pow(d.clamp_min(1e-6),-0.5)); return inv@a@inv
