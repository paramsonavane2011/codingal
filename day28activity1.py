class IOString():
    def __init__(self, str1="abc"):
        self.str1 = str1
    def IOinput(self):
        self.str1 = input("Enter your preferred value for string: ")
    def printSelf(self):
        print(f"Result is: {self.str1.upper()}")

obj1 = IOString("Hi")
obj2 = IOString()

obj1.printSelf()
obj2.IOinput()
obj2.printSelf()