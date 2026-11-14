class TimeEngine:
    def __init__(self,delta_time=0.1):
        self.time=0.0
        self.delta_time=delta_time
    def update(self):
        self.time+=self.delta_time
        return self.time
    def reset(self):
        self.time=0.0

if __name__=="__main__":
    obj=TimeEngine()
    print(TimeEngine.update)
        