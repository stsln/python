import turtle

turtle.shape('turtle')
x = 0
for i in range(10):
    for a in range(4):
        turtle.forward(25 + x)
        turtle.left(90)
    x += 10
    turtle.penup()
    turtle.backward(5)
    turtle.right(90)
    turtle.forward(5)
    turtle.left(90)
    turtle.pendown()
