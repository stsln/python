import turtle
import math

turtle.shape('turtle')
k = 1
fi_rad = 0.3
fi_degr = fi_rad * (180 / math.pi)
for i in range (1000):
    ro = k * fi_rad
    turtle.forward(ro)
    turtle.left(fi_degr)
    fi_rad += 0.1
    ro += ro
