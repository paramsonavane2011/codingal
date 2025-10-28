marks1 = int(input("Enter marks of subject 1: "))
marks2 = int(input("Enter marks of subject 2: "))
marks3 = int(input("Enter marks of subject 3: "))
marks4 = int(input("Enter marks of subject 4: "))
marks5 = int(input("Enter marks of subject 5: "))

average = (marks1 + marks2 + marks3 + marks4 + marks5) / 5

avg = average / 10 * 100

if 91 <= avg <= 100:
    print("Grade A1")
elif 81 <= avg < 91:
    print("Grade A2")
elif 71 <= avg < 81:
    print("Grade B1")
elif 61 <= avg < 71:
    print("Grade B2")
elif 51 <= avg < 61:
    print("Grade C1")
elif 41 <= avg < 51:
    print("Grade C2")
elif 31 <= avg < 41:
    print("Grade D1")
elif 21 <= avg < 31:
    print("Grade D2")
elif 11 <= avg < 21:
    print("Grade E1")
elif 0 <= avg < 11:
    print("Grade E2")
else:
    print("Invalid marks")
