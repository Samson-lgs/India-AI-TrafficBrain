from trafficbrain.evaluation.metrics import compute_metrics
def test_metrics():
    x=compute_metrics({'waiting_seconds':[1,3],'queues':[2,4],'spillback_events':1}); assert x['mean_waiting_seconds']==2.0 and x['mean_queue']==3.0
