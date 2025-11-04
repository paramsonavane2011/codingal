med = input("Were you medically sick? (yes/no): ").strip().lower()
if med == "yes":
    print("You are allowed to reappear for the exam.")
elif med == "no":
    attendance = int(input("Enter your attendance percentage: ").strip())
    if attendance >= 75:
        print("You are allowed to appear for the exam.")
    else:
        print("You are not allowed to appear for the exam due to low attendance.")