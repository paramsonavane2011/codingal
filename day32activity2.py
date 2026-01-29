class Flashcard():
    def __init__(self, w, m):
        self.word = w
        self.meaning = m
    def __str__(self):
        return f"{self.word}: {self.meaning}"

list = []

while True:
    w = input("Enter a word: ")
    m = input("Enter its meaning: ")
    list.append(Flashcard(w, m))
    c = input("Do you wanna add more words?(y/n): ")
    if c == "n":
        break

print("Your words: ")
for i in list:
    print(f"  > {i}")