class employee():
    def __init__(self, name, id):
        self.name = name
        self.id = id
        print("constructor")
    def getID(self):
        print(f"ID: {self.id}")
    def __del__(self):
        print("destructor")
    
obj = employee("xyz", 69)
del obj

obj1 = employee("abc", 69)
obj1.getID()