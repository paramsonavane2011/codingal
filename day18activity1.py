try:
    num = int(input("Enter a number: "))
    print(f"The number you entered is {num}")
except ValueError as e:
    print(f"Exception: {e}")