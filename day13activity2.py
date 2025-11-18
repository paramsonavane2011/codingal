rows = int(input("Enter required number of rows: "))
count = 0
num = 0

for a in range(0, rows + 1):
    for b in range(0, a):
        num += 1
        print(f"{num}", end=" ")
    print()
    count += 1
