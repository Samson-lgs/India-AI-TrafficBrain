import argparse
from trafficbrain.simulation.environment import TrafficNetwork
from trafficbrain.simulation.baseline import FixedTimeController,PressureController

def main():
    p=argparse.ArgumentParser(); p.add_argument('--controller',choices=['fixed','pressure'],default='pressure'); p.add_argument('--steps',type=int,default=300); a=p.parse_args()
    e=TrafficNetwork(seed=7); c=FixedTimeController(e) if a.controller=='fixed' else PressureController(e); total=0.0
    for _ in range(a.steps):
        o=e.observe(); e.step(c.act(o)); total+=sum(o['waiting_seconds'])
    print({'controller':a.controller,'steps':a.steps,'total_wait_proxy':round(total,2),'vehicles':e.total_vehicles()})
if __name__=='__main__': main()
