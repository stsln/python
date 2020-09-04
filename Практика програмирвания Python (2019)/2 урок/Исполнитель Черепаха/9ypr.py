import turtle
import math

turtle.shape('turtle')
turtle.right(90)
n = 3
r = 10
a = r * (2 * math.sin(6 / n))

for i in range (2):
    k = n
    while k > 0:
        turtle.forward(a)
        turtle.left(360 / n)
        k -= 1
                    
    turtle.penup()
    turtle.backward(r)
    turtle.left(60)
    turtle.pendown()
    
    n += 1
    a += 20
    r *= 2
