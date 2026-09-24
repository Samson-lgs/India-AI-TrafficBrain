from trafficbrain.simulation.environment import TrafficNetwork
def test_progresses():
    e=TrafficNetwork(seed=1); t=e.time; e.step([]); assert e.time==t+1
