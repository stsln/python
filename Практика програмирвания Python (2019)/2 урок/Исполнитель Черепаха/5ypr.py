import turtle

turtle.shape('turtle')
x = 0
a = 0
b = 0

while b != 10:
    while a != 4:
        turtle.forward(25 + x)
        turtle.left(90)
        a += 1
    turtle.penup()   
    turtle.backward(5)
    turtle.right(90)
    turtle.forward(5)
    turtle.left(90)
    turtle.pendown()
    x += 10
    a = 0
    b += 1

