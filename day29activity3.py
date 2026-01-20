class bird():
    def __init__(self):
        print("Hello")
    def fly(self):
        print("Flying..")
    def walk(self):
        print("Walking..")

class parrot(bird):
    def __init__(self):
        super().__init__()
    def fly(self):
        print("Flying..")
    def walk(self):
        print("Walking..")

parrot1 = parrot()
parrot1.walk()