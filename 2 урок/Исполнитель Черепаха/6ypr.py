import turtle

turtle.shape('turtle')
x = 0
b = 0
n = 12
while b != n:
    turtle.forward(100)
    turtle.stamp()
    turtle.backward(100)
    turtle.left(360 / n)
    b += 1
