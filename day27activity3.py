class parrot:
    food = "mangoes"
    shelter = "nest"
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = parrot("p1", 3)
p2 = parrot("p2", 4)
p3 = parrot("p3", 3)

print(p1.food, p2.shelter)
print(p1.name, p1.age)
print(p2.name, p2.age)
print(p3.name, p3.age)