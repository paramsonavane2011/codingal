num = int(input("Enter number for its factorial: "))

def fact(num):
    """This is a \"docstring\""""
    if num == 0 or num == 1:
        return 1
    else:
        factorial = num * fact(num - 1)
        return factorial

print(fact.__doc__)
print(f"The factorial for {num} is {fact(num)}")