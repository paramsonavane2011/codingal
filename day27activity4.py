class shape:
    def __init__(self, height, radius):
        self.h = height
        self.r = radius
    def volume(self):
        print(2 * 3.14 * self.r * self.h)
        
cone1 = shape(5, 7)
print(cone1.h)
print(cone1.r)
cone1.volume()

cone2 = shape(5, 12)
print(cone2.h)
print(cone2.r)
cone2.volume()