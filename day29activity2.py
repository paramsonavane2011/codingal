class person():
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def display(self):
        print(f"Name: {self.name}\nID: {self.id}")

class employee(person):
    def __init__(self, name, id, salary, post):
        self.salary = salary
        self.post = post
        super().__init__(name, id)

person1 = employee("qwerty", 123456, "15500/m", "Assistant To The Manager")
person1.display()