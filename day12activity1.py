w = input("Enter a word: ")
c = input("Enter a character from your given input: ")
count = 0

for a in w:
    if c == a:
        count += 1

print(f"\"{c}\" occured {count} times in \"{w}\".")