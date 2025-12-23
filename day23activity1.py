students = {
    "id1": {"name": "Alice", "age": 20, "grade": "A"},
    "id2": {"name": "Bob", "age": 22, "grade": "B"},
    "id3": {"name": "Charlie", "age": 23, "grade": "C"},
    "id4": {"name": "Alice", "age": 20, "grade": "A"}
}

studentsCopy = students.copy()

names = []

for key, value in studentsCopy.items():
    if value["name"] in names:
        students.pop(key)
    else:
        names.append(value["name"])

print(students)