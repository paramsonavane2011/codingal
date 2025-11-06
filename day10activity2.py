word = input("Enter a word: ")

rev = ""

for a in word:

    rev = a + rev

print(f"The reverse of the word \"{word}\" is \"{rev}\".")