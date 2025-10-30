num = int(input("Enter numerator: "))
den = int(input("Enter denominator: "))

if num % den == 0:
    print(f"{num} is exactly divisible by {den}")
else:
    print(f"{num} is not exactly divisible by {den}")
