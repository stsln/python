###Условный оператор
PyCarm Community Ed.

if условие:
	оператор 1
	оператор 2
elif y > 0:
	
else:

Лучше отсутствие комментаия, чем устаревший комментарий.

x = int(input()) 
while x > 0: #заголовок цикла
	print(x) #тело цикла
	x -= 1
#x <= 0 

while x > 0:
	x -= 1
	if x == 13:
		break
	print(x)
#x <= 0 или x == 13

###Цикл for
Это цикл не зацикличен.

for x in 1, 5, 2, 4, 3:  #1, 5, 2, 4, 3 - это кортеж (итеируемый объект)
	print(x ** 2)

x = 1
while x < 101:
	print(x)
	x += 1

for x in range(start, stop, step): #range - генератор арифметической прогресcии; по умол. start = 0, step = 1
	print(x)

>>> A = range(1, 100, 2)
>>> print(A)
range(1, 100, 2)
>>> type(A)
<class 'range'>

###Функции

def f(x, y): #x и y - это формальные параметры
	return x + y
print(f(1, 2))

>>> def f(x, y):
	return x + y
>>> print(f(1, 2))
3
>>> print(f(1, f(2, 3)))
6
>>> print(f('2', '3'))
23
>>> print(f(2, 2.5))
4.5

Полиморфизм - DuckTyping

Аннотация в коде:
def f(x: int, y: int): 
	return x + y

def p3(x):
	print(x)
	print(x)
	print(x)
x = p3('Hello')

>>> def p3(x):
	print(x)
	print(x)
	print(x)
>>> x = p3('Hello')
Hello
Hello
Hello
>>> type(x)
<class 'NoneType'>

PEP8 
Лучше пользоваться PyCarm Community Ed., где есть поверка кода.
"""Многострочный
комментаий.
"""