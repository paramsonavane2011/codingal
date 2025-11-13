s = int(input("Enter first number: "))
e = int(input("Enter final number: "))

for num in range(s, e + 1):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)
        