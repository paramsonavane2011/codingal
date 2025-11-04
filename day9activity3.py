v = int(input("Choose bike(1) or car(2): "))

if v == 1:
    choice = int(input("Choose motorbike(1) or scooter(2): "))
    if choice == 1:
        print("You have chosen motorbike.")
    elif choice == 2:
        print("You have chosen scooter.")
    else:
        print("Invalid choice for bike.")
elif v == 2:
    choice = int(input("Choose sedan(1) or suv(2): "))
    if choice == 1:
        print("You have chosen sedan.")
    elif choice == 2:
        print("You have chosen suv.")
    else:
        print("Invalid choice for car.")
else:
    print("Invalid input.")