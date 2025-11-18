rows = int(input("Enter required number of rows: "))
spaces = rows // 2
count = 1
z = spaces + 1

for a in range(0, spaces):
    print(" " * spaces + "*" * count + " " * spaces)
    count += 2
    spaces -= 1

spaces = 0
count = rows

for b in range(0, z):
    print(" " * spaces + "*" * count + " " * spaces)
    count -= 2
    spaces += 1