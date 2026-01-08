class vehicle:
    def __init__(self, max, economy):
        self.speed = max
        self.mileage = economy

vehicle1 = vehicle(69, "6.9km/l")
print(vehicle1.speed, vehicle1.mileage)