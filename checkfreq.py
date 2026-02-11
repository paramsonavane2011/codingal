dict = {
    "Codingal": 3,
    "is": 2,
    "best": 2,
    "for": 2,
    "coding": 1
}

# dict = dict.items()

i = input("Enter a word: ")

if i in dict:
    print("The frequency of the word is:", dict[i])
else:
    print("The word is not present in the dictionary.")