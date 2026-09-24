import torch

def synthetic_graph_batch(nodes=6,history=12,horizon=6,batch=32):
    x=torch.rand(batch,history,nodes,4); y=torch.rand(batch,horizon,nodes,1); adj=torch.zeros(nodes,nodes)
    for i in range(nodes-1): adj[i,i+1]=adj[i+1,i]=1
    return x,y,adj
