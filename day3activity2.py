name = "Param"
age = 13
is_student = True
weight = 46

print("Name:", name)
print("Data type of name:", type(name))

print("Age:", age)
print("Data type of age:", type(age))

print("Is Student:", is_student)
print("Data type of is_student:", type(is_student))

print("Weight:", weight)
print("Data type of weight:", type(weight))

print("After type casting:")

age = str(age)
print("Data type of age after type casting:", type(age))

weight = int(weight)
print("Data type of weight after type casting:", type(weight))