import turtle

turtle.shape('turtle')
turtle.left(90)
turtle.pen(fillcolor="yellow", pencolor="black")
turtle.begin_fill()
for i in range(72):
    turtle.forward(10)
    turtle.left(5)
turtle.end_fill()


def eyes():
    for j in range(72):
        turtle.forward(1.5)
        turtle.left(5)


turtle.pen(fillcolor="blue", pencolor="black")
turtle.begin_fill()
turtle.penup()
turtle.goto(-150, 50)
turtle.pendown()
eyes()
turtle.end_fill()

turtle.begin_fill()
turtle.penup()
turtle.goto(-50, 50)
turtle.pendown()
eyes()
turtle.end_fill()

turtle.penup()
turtle.width(10)
turtle.goto(-120, 10)
turtle.pendown()
turtle.backward(50)

turtle.penup()
turtle.width(10)
turtle.color('red')
turtle.goto(-180, -40)
turtle.pendown()
turtle.circle(-60, -180)
