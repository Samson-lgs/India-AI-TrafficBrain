def compute_metrics(history):
    waits=history.get('waiting_seconds',[]); queues=history.get('queues',[])
    return {'mean_waiting_seconds':sum(waits)/len(waits) if waits else 0.0,'mean_queue':sum(queues)/len(queues) if queues else 0.0,'throughput_proxy':history.get('throughput_proxy',0.0),'spillback_events':history.get('spillback_events',0),'estimated_co2_g':history.get('estimated_co2_g',0.0)}
