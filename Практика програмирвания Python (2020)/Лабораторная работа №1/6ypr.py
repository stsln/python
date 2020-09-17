import turtle

turtle.shape('turtle')
n = 12
for i in range(n):
    turtle.forward(100)
    turtle.stamp()
    turtle.backward(100)
    turtle.left(360 / n)
