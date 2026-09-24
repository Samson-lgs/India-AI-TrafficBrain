from trafficbrain.perception.state import TrafficStateEstimator

d=[{'class_name':'car','speed_kph':0},{'class_name':'bike','speed_kph':10},{'class_name':'bus','speed_kph':0}]
print(TrafficStateEstimator().from_detections(d))
