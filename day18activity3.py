while True:
    try:
        num = int(input("Enter a number: "))
        while num % 2 == 0:
            print("even")
        while num % 2 != 0:
            print("odd")
    except ValueError:
        print("Incorrect input")