c1 = input("Is task 1 complete? (y/n): ")
c2 = input("Is task 2 complete? (y/n): ")
if c1.lower() == 'y' and c2.lower() == 'y':
    print("All tasks complete. Proceeding to shutdown.")
elif c1.lower() == 'y' or c2.lower() == 'y':
    print("One task complete. Please complete the remaining task before shutdown.")
else:
    print("sorry")