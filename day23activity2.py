dict = {
    "Hi": 3,
    "Hello": 5,
    "Hey": 3,
    "Howdy": 4
}

i = 3
count = 0

for key in dict:
    if dict[key] == i:
        count += 1
        print(key)

print(f"Words with frequency {i}: {count}")