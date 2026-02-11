class BMV():
    def __init__(self):
        self.fuelType = "Diesel"
        self.maxSpeed = 250

class Ferrari():
    def __init__(self):
        self.fuelType = "Petrol"
        self.maxSpeed = 350

c1 = BMV()
c2 = Ferrari()

for a in (c1, c2):
    print(a.fuelType, a.maxSpeed)