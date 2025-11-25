def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

operation = input("Select an operation(+, -, *, /): ").lower().strip()
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

if operation == "+":
    result = add(num1, num2)
if operation == "-":
    result = subtract(num1, num2)
if operation == "*":
    result = multiply(num1, num2)
if operation == "/":
    result = divide(num1, num2)

print(f"{num1} {operation} {num2} = {result}")