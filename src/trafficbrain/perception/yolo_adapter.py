class YOLOAdapter:
    def __init__(self,model): self.model=model
    def parse(self,results):
        return [{'class_name':str(results.names[int(b.cls.item())]),'confidence':float(b.conf.item())} for b in results.boxes]
