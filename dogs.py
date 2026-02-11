class Dog():
    def __init__(self, colour, breed):
        self.colour = colour
        self.breed = breed

    def details(self):
        return f"Colour: {self.colour}, Breed: {self.breed}"

dog1 = Dog("Brown", "Labrador")
print(dog1.details())
dog2 = Dog("Black", "German Shepherd")
print(dog2.details())