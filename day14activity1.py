import turtle

sides = int(input("Enter number of sides for polygon: "))

turtle.Screen().setup(600, 400)
polygon = turtle.Turtle()

angle = 360 / sides

for a in range(0, sides):
    polygon.forward(50)
    polygon.right(angle)

turtle.done()