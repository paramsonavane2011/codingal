class Vehicle():
    def __init__(self, sc):
        self.sc = sc
    def fare(self):
        return self.sc * 100

class Bus(Vehicle):
    def fare(self):
        return super().fare() * 1.1

bus = Bus(50)
print(bus.fare())