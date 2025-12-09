import random

choices = ["rock", "paper", "scissors"]
shoot = input("Choose between rock, paper, and scissors: ").lower().strip()
com = random.choice(choices)

if shoot == "rock":
    if com == "scissors":
        print(f"Computer chose {com}, you won!")
    elif com == "paper":
        print(f"Computer chose {com}, you lost..")
    else:
        print(f"Computer chose {com}, it\'s a tie.")

if shoot == "paper":
    if com == "rock":
        print(f"Computer chose {com}, you won!")
    elif com == "scissors":
        print(f"Computer chose {com}, you lost..")
    else:
        print(f"Computer chose {com}, it\'s a tie.")

if shoot == "scissors":
    if com == "paper":
        print(f"Computer chose {com}, you won!")
    elif com == "rock":
        print(f"Computer chose {com}, you lost..")
    else:
        print(f"Computer chose {com}, it\'s a tie.")