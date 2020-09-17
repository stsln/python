from turtle import Turtle
import math

t = Turtle()
t.speed(10)
t.shape('turtle')

k = 1
fi_radian = 30
for i in range(1000):
    p = k * fi_radian
    t.forward(p)
    t.left(90)
    fi_radian += 5
