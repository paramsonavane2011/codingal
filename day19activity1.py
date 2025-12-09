import random

num = random.randint(10, 20)

while True:
    guess = int(input("Enter a number between 10 and 20: "))
    if guess == num:
        print(f"You guessed the number {num}!")
        break
    else:
        print("Try again..")