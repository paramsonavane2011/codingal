start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
even = []
odd = []

for a in range(start, end + 1):
    sq = a ** 2
    if sq % 2 == 0:
        even.append(sq)
    else:
        odd.append(sq)

print("Even squares:", even)
print("Odd squares:", odd)