import turtle

turtle.Screen().setup(800, 600)

shape = turtle.Turtle()
dis = 10

for a in range(0, 50):
    shape.forward(dis)
    shape.right(90)
    dis += 5

turtle.done()