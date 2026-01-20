class vehicle():
    def __init__(self, name, maxSpeed, mileage):
        self.name = name
        self.maxSpeed = maxSpeed
        self.mileage = mileage

class bus(vehicle):
    pass

schoolBus = bus("Volvo", 80, "8.5km/l")
print(f"Name: {schoolBus.name}\nMax speed: {schoolBus.maxSpeed}\nMileage: {schoolBus.mileage}")