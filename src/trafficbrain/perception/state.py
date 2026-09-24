from collections import Counter
from dataclasses import dataclass

PCE={'car':1.0,'bike':0.5,'auto':1.0,'bus':2.5,'truck':3.0,'bicycle':0.3}
@dataclass
class TrafficState:
    vehicle_count:int
    queue_estimate:float
    mean_speed_kph:float
    stopped_count:int
    pce_load:float
    class_distribution:dict
class TrafficStateEstimator:
    def from_detections(self,detections):
        speeds=[float(d.get('speed_kph',0)) for d in detections]; classes=[d.get('class_name','car') for d in detections]
        stopped=sum(s<=2 for s in speeds)
        return TrafficState(len(detections),float(stopped),sum(speeds)/len(speeds) if speeds else 0.0,stopped,sum(PCE.get(c,1) for c in classes),dict(Counter(classes)))
