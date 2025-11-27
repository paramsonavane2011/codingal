bill = int(input("Enter amount to be paid for tip calculation: "))
tip = int(input("Enter tip percentage: "))

def tipCalc(a, b):
    total = a + (a * b / 100)
    return round(total)

print(f"The total is {tipCalc(bill, tip)}")