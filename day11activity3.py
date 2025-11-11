num = int(input("Enter a number: "))
final = 0
print(num)
n = str(num)

for a in n:
    final += int(a) ** len(n)

if final == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")