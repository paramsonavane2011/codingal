import turtle

turtle.Screen().setup(800, 600)

shape = turtle.Turtle()

for a in range(0, 5):
    shape.forward(100)
    shape.right(180 - 36)

turtle.done()