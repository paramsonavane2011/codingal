currentMean = float(input("Enter current mean: "))
numbers = int(input("Enter number of values: "))
incorrectNumber = float(input("Enter incorrect number: "))
correctNumber = float(input("Enter correct number: "))


if incorrectNumber > correctNumber:

    newMean = ((currentMean * numbers) -
               (incorrectNumber - correctNumber)) / numbers

else:
    newMean = ((currentMean * numbers) -
               (correctNumber - incorrectNumber)) / numbers

print(newMean)
