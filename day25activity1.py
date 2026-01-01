n1 = [1, 2, 3]
n2 = [4, 5, 6]
result = map(lambda a, b: a + b, n1, n2)
print(list(result))

num = [1, 2, 3, 4, 5]
def s(num):
    return num ** 2
sq = map(s, num)
print(list(sq))