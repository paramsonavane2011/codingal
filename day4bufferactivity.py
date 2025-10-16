days = int(input("Enter numebr of days to be converted into years/weeks/days: "))

daysToConvert = days

noOfyears = days // 365

days -= noOfyears * 365

noOfweeks = days // 7

days -= noOfweeks * 7

print(f"\n{daysToConvert} days is {noOfyears} years, {noOfweeks} weeks, {days} days.")
