num = int(input("Enter a number: "))
odd = []
for i in range(1, num + 1):
    if i % 2 != 0:
        odd.append(i)
print(odd)

fruits = ["apple", "banana", "cherry", "date", "strawberry"]
res = []
for i in fruits:
    res.append(i.capitalize())

print(res)