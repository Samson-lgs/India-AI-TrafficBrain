from types import SimpleNamespace
from trafficbrain.control.safety import SafetyShield
def test_safety_clamps():
    s=SafetyShield().validate(None,[SimpleNamespace(junction_id=0,delta_green=99)]); assert s[0].delta_green==5
