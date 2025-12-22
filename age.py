age = input("Please enter your age: ")

if age == int(age):
    print("You entered a valid age.")
    if age % 2 == 0:
        print("Your age is an even number.")
    else:
        print("Your age is an odd number.")
else:
    raise ValueError