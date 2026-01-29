import random

class FruitQuiz():
    def __init__(self):
        self.fruits = {
            "apple": "red",
            "orange": "orange",
            "banana": "yellow",
            "kiwi": "brown"
        }
    def quiz(self):
        while True:
            fruit, colour = random.choice(list(self.fruits.items()))
            que = input(f"Enter the colour of a/an {fruit}: ")
            if que.strip().lower() == colour:
                print("You got it!")
            else:
                print("Try again..")
                continue
            c = input("Do you want to play more?(y/n): ")
            if c.strip().lower() != "y":
                break

obj = FruitQuiz()
obj.quiz()