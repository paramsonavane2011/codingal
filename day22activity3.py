weather = (1, 0, 1, 0, 1, 0, 0)

rainy = weather.count(0)
sunny = weather.count(1)

print(f"Rainy: {rainy}")
print(f"Sunny: {sunny}")

if sunny > rainy:
    print("The weather is good")
else:
    print("The weather is bad")