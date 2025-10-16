amount = int(input("Enter the amount of money: "))

noOf100 = amount // 100

amount -= noOf100 * 100

noOf50 = amount // 50

amount -= noOf50 * 50

noOf20 = amount // 20

amount -= noOf20 * 20

noOf10 = amount // 10

amount -= noOf10 * 10

print(f"Number of 100 rupee notes: {noOf100}")
print(f"Number of 50 rupee notes: {noOf50}")
print(f"Number of 20 rupee notes: {noOf20}")
print(f"Number of 10 rupee notes: {noOf10}")
print(f"Remaining money {amount}")
