eng = int(input("Enter english marks: "))
hin = int(input("Enter hindi marks: "))
mat = int(input("Enter math marks: "))
sci = int(input("Enter science marks: "))
maxmarks = int(input("Enter maximum marks: "))

overall = (eng + hin + mat + sci) / 4

percentage = overall / maxmarks * 100

print(f"Overall percentage is {percentage}")
