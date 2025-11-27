def cube(num):
    c = num ** 3
    return c

def cubeMod(n):
    if n % 3 == 0:
        return cube(n)
    else:
        return None
    
print(cubeMod(3))
print(cubeMod(4))