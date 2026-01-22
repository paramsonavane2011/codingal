class Parent():
    def __init__(self):
        self.a = "ABC"
        self._c = "DEF"

class Child(Parent):
    def __init__(self):
        super().__init__()
        print(self._c)

parent = Parent()
print(parent._c)
child = Child()