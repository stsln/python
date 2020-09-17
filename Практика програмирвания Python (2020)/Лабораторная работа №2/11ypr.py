import turtle

turtle.shape('turtle')
turtle.left(90)
for i in range(10):
    turtle.circle(30 + i * 5)
    turtle.circle(-(30 + i * 5))
