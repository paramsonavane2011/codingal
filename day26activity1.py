import random

num = random.randint(1, 100)
print(num)
tries = 0

name = input("What's your name? -> ")
print(f"Okay {name}, we will play a game where you guess a number between 1 and 100.")

while True:
    tries += 1
    g = input("Enter your guess -> ")
    guess = int(g)
    if (100 >= guess >= 1) and (guess != num):
        print("Try again.")
    elif guess == num:
        print(f"Well done! You guessed {num} in {tries} {"tries" if tries > 1 else "try"}.")
        break
    elif 100 < guess < 1:
        print("Try again, and be in the range.")
    else:
        print("Your input is not a number.")