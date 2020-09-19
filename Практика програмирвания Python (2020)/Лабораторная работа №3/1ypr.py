from turtle import Turtle
from random import *

t = Turtle()
t.speed(10)
t.shape('turtle')

n = 50
for i in range(n):
    t.forward(randint(-30, 30))
    t.left(randint(0, 360))
    t.backward(randint(-30, 30))
    t.right(randint(0, 360))
