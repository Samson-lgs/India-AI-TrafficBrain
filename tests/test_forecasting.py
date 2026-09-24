from trafficbrain.forecasting.dataset import synthetic_graph_batch
from trafficbrain.forecasting.model import TemporalGraphForecaster
def test_forecaster_shape():
    x,y,a=synthetic_graph_batch(batch=2); assert TemporalGraphForecaster()(x,a).shape==y.shape
