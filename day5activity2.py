cp = float(input("Enter the cost price of the item: "))
sp = float(input("Enter the selling price of the item: "))

if sp > cp:
    print("Profit is {0}".format(sp - cp))
elif cp > sp:
    print("Loss is {0}".format(cp - sp))
else:
    print("No profit or loss")