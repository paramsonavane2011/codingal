try:
    num1, num2 = eval(input("Enter 2 numbers separated by commas: "))
    res = num1 / num2
    print(f"Result is: {num1} / {num2} = {res}")
except ZeroDivisionError:
    print("Cannot divide by 0")
except SyntaxError:
    print("Comma was not used")
except:
    print("Input contained something other than numbers")