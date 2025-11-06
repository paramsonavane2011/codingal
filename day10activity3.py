num = int(input("Enter a number: "))

list = range(1, num + 1)

for i in list:
    print(list[-i])