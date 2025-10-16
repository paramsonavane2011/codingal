count = 0
total = 0
while count < 5:
    num = int(input("Enter a number: "))
    total += num
    count += 1

average = total / count
print(f"Average is {average}")
