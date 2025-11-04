units = int(input("Enter number of units consumed: "))
cost = 0

if units <= 50:
    cost = units * 2.6 + 25
    print(f"The cost is {cost}")
elif 50 < units <= 100:
    cost = (units - 50) * 3.25 + 35 + 130
    print(f"The cost is {cost}")
elif 100 < units <= 200:
    cost = (units - 100) * 5.26 + 45 + 130 + 162.5
    print(f"The cost is {cost}")
elif 200 < units:
    cost = (units - 200) * 8.45 + 75 + 130 + 162.5 + 526
    print(f"The cost is {cost}")