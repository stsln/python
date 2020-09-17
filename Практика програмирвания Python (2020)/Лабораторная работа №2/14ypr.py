import turtle

turtle.shape('turtle')
n = 5
while True:
    turtle.forward(150)
    turtle.left(180 - (360 / n) / 2)
    if abs(turtle.pos()) < 1:
        break

turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()

n = 11
while True:
    turtle.forward(150)
    turtle.left(180 - (360 / n) / 2)
    if abs(turtle.pos()) == 200.00000000000003:
        break
turtle.done()
