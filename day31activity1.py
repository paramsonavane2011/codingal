from abc import ABC, abstractmethod

class Abstraction(ABC):
    def print(self, i):
        print(f"Value: {i}")
    @abstractmethod
    def task(self):
        print("You are in Abstraction")

class Test(Abstraction):
    def task(self):
        print("You are in Test")
        super().task()

obj = Test()
obj.task()
obj.print(69)
# obj1 = Abstraction()
# obj1.task()