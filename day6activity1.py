eng = int(input("Enter marks in English: "))
math = int(input("Enter marks in Math: "))
sci = int(input("Enter marks in Science: "))

if eng > 60 and math > 60 and sci > 60:
    print("You are in the 1st Division")
    
elif ((eng > 50 and eng < 60) and (math > 50 and math < 60)) or ((eng > 50 and eng < 60) and (sci > 50 and sci < 60)) or ((math > 50 and math < 60) and (sci > 50 and sci < 60)):
    print("You are in the 2nd Division")

elif (eng < 50 and math < 50) or (eng < 50 and sci < 50) or (math < 50 and sci < 50):
    print("You are in the 3rd Division")