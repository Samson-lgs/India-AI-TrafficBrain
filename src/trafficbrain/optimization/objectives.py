def network_objective(metrics,weights=None):
    w=weights or {'delay':1.0,'queue':1.0,'spillback':2.0,'co2':0.2,'fairness':0.5}
    return w['delay']*metrics.get('mean_waiting_seconds',0)+w['queue']*metrics.get('mean_queue',0)+w['spillback']*metrics.get('spillback_events',0)+w['co2']*metrics.get('estimated_co2_g',0)
