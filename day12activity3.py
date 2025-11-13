num = input("Enter a number: ")
num = list(num)
final = 1

if len(num) >= 4:
    num.pop(0)
    num.pop(-1)
else:
    print("Invalid input.")
    quit()

for a in num:
    final *= int(a)

print(final)