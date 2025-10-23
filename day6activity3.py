weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in centimeters: "))

bmi = weight / ((height / 100) ** 2)

if bmi < 18.5:
    print("You are underweight")
elif bmi <= 24.9:
    print("You have a normal weight")
elif bmi <= 29.9:
    print("You are overweight")
elif bmi <= 34.9:
    print("You are severely overweight")
elif bmi <= 39.9:
    print("You are obese")
else:
    print("You are severely obese")