import array as ar

a = ar.array('i', [1, 2, 3, 4, 5, 3, 4, 3])
print(a)
print(a.count(4))
a.reverse()
print(a)