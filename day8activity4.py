speed1 = int(input("Enter speed of first car (in km/h): "))
speed2 = int(input("Enter speed of second car (in km/h): "))
speed3 = int(input("Enter speed of third car (in km/h): "))

avg = (speed1 + speed2 + speed3) / 3

if speed1 < avg:
    print(f"Car 1 is below average speed with {speed1} km/h")
if speed2 < avg:
    print(f"Car 2 is below average speed with {speed2} km/h")
if speed3 < avg:
    print(f"Car 3 is below average speed with {speed3} km/h")
