import turtle
import math

turtle.shape('turtle')

n = 10  # сколько нужно нарисовать правильных n-угольников
angles = 3  # количество углов
r = 20  # радиус описанной окружности
step = 20  # расстояние между описываемыми окружностями

for i in range(n):
    length = 2 * r * math.sin(math.pi / angles)
    turtle.left((180 - (360 / angles)) / 2)
    for j in range(angles):
        turtle.left(360 / angles)
        turtle.forward(length)
    turtle.right((180 - (360 / angles)) / 2)
    turtle.penup()
    turtle.forward(step)
    turtle.pendown()

    angles += 1
    r += step
