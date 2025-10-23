age1 = int(input("Enter age of person 1: "))
age2 = int(input("Enter age of person 2: "))
age3 = int(input("Enter age of person 3: "))
if age1 != age2 and age1 != age3 and age2 != age3:
    print("They are of different ages")
elif age1 == age2 and age1 == age3:
    print("All three are of same age")
else:
    print("Two people are of same age")


num = int(input("Enter a number: "))
if (num % 2) != 0:
    print("The number is odd")
else:
    print("The number is even")