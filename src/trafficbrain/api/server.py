from fastapi import FastAPI
from trafficbrain.simulation.environment import TrafficNetwork
from trafficbrain.simulation.baseline import PressureController
app=FastAPI(title='India AI TrafficBrain',version='0.1.0')
@app.get('/health')
def health(): return {'status':'ok'}
@app.get('/simulate')
def simulate(steps:int=120):
    env=TrafficNetwork(seed=11); ctl=PressureController(env); total=0.0
    for _ in range(steps):
        obs=env.observe(); env.step(ctl.act(obs)); total+=sum(obs['waiting_seconds'])
    return {'steps':steps,'total_wait_proxy':round(total,2),'vehicles':env.total_vehicles()}
