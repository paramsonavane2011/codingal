s1 = {1, 2, 3, 4, 5}
s2 = {"hi", 0, 4.5, (1, 2)}
s3 = {True, False, None}
s4 = {0, 1, 2, 3, 4}

print(s1 & s4)
print(s1.intersection(s4))
s1.pop()
print(s1)