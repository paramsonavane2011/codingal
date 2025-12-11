def rentalCar(days: int):
    return days * 50

def planeRide(city: str):
    if city.lower() == "mumbai":
        return 7000
    elif city.lower() == "delhi":
        return 5000
    else:
        return 0
    
def hotel(days: int):
    return days * 1200

def tripCost(days, city, money):
    return rentalCar(days) + planeRide(city) + hotel(days) + money

print(tripCost(5, "Mumbai", 4000))