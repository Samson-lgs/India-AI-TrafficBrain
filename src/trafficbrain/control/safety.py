class SafetyShield:
    def __init__(self,min_green=10,max_green=60): self.min_green=min_green; self.max_green=max_green
    def validate(self,env,actions):
        safe=[]
        for a in actions:
            delta=max(-5,min(5,int(a.delta_green))); safe.append(type(a)(junction_id=a.junction_id,delta_green=delta))
        return safe
