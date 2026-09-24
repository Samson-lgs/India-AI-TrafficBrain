from trafficbrain.perception.state import TrafficStateEstimator
def test_state():
    s=TrafficStateEstimator().from_detections([{'class_name':'car','speed_kph':0},{'class_name':'bike','speed_kph':10}]); assert s.vehicle_count==2 and s.stopped_count==1 and s.pce_load>1
