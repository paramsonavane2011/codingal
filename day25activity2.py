l1 = [1, 2, 3]
l2 = [4, 5, 6]
l = list(zip(l1, l2))
print(l)

for a, b in zip(l1, l2[::-1]):
    print(f"{a} -> {b}")

stocks = ["a", "b", "c"]
prices = [1, 2, 3]

d = {s: p for s, p in zip(stocks, prices)}
print(d)