import turtle
import ast
from random import *

window = turtle.Screen()

t = turtle.Turtle()
t.shape('turtle')
t.color('blue')
t.width(2)

with open('3_2ypr.txt', 'r') as digits:
    digits = digits.read()
digits = ast.literal_eval(digits)


def font_mail(text):
    for key, elem in enumerate(text):
        if elem in digits:
            t.penup()
            start_x, start_y = digits[elem][0]  # start_x и start_y присваиваем значения начальных координат цифры
            right_x = 50 * key  # сумма пикселей, которые являются промежутками между цифрами
            t.setpos(right_x + start_x, start_y)  # устанавливаем позицию откуда нужно начинать рисование
            t.pendown()

            for x, y in digits[elem][1:]:
                t.setpos(right_x + x, y)


font_mail('141700')
window.mainloop()
