import numpy as np
from .dqn import MultiAgentDQN,Transition
from ..simulation.environment import TrafficNetwork

def train_smoke_dqn(episodes=5):
    env=TrafficNetwork(seed=3); agent=MultiAgentDQN(); losses=[]
    for _ in range(episodes):
        state=env.reset()['queues'].flatten(); state=np.pad(state,(0,32-len(state)))[:32].astype(np.float32)
        for _ in range(10):
            action=agent.select(state,.2); ns=env.step([])['queues'].flatten(); next_state=np.pad(ns,(0,32-len(ns)))[:32].astype(np.float32); reward=-float(env.observe()['queues'].mean()); agent.memory.append(Transition(state,action,reward,next_state,False));
            if len(agent.memory)>=4: losses.append(agent.update(agent.memory[-4:]))
            state=next_state
    return {'episodes':episodes,'updates':len(losses),'last_loss':losses[-1] if losses else None}
