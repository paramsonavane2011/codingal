str = input("Enter a string: ")

for a in str:
    if a.lower == "a":
        print("\"a\" has been found")
        break

if "a" not in str.lower: 
    print("No \"a\" in given string")