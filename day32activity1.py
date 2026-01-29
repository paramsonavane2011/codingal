class I():
    def __init__(self, i):
        self.i = i
    def __lt__(self, un):
        if self.i < un.i:
            return f"{self.i} < {un.i}"
        else:
            return f"{self.i} > {un.i}"
    def  __eq__(self, un):
        if self.i == un.i:
            return f"{self.i} == {un.i}"
        else:
            return f"{self.i} != {un.i}"
    
obj1 = I(6)
obj2 = I(9)
print(obj1 < obj2)
print(obj1 == obj2)