from turtle import Turtle
import math

t = Turtle()
t.speed(100_000)
t.shape('turtle')

k = 1
fi_radian = 0.3
fi_step = fi_radian * (180 / math.pi)
for i in range(1000):
    p = k * fi_radian
    t.forward(p)
    t.left(fi_step)
    fi_radian += 0.1
