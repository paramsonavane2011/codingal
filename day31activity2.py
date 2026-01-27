from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can walk, run, and swim.")

class Cat(Animal):
    def move(self):
        print("I can walk, run, and climb.")

class Dog(Animal):
    def move(self):
        print("I can walk, run, and bark.")

class Horse(Animal):
    def move(self):
        print("I can walkand run really fast.")

a = Human()
a.move()
b = Cat()
b.move()
c = Dog()
c.move()
d = Horse()
d.move()
