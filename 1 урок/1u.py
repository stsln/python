###Операторы в Python

'+', '-', '*', '/', '//', '**'

>>> 2 + 2
4
>>> type(2 + 2)
class <int>

>>> 2 / 3

>>> type(2/3)
class <float>

>>> 14 // 3
4
>>> 14 % 3

>>> 2 ** 10
1024
>>> 2 ** 100
1267650600228229401496703205376
>>> 2 ** 1000
10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376

>>> type(2 / 3)
<class 'float'>
>>> 'Hello'
'Hello'
>>> 'Hello' + 'World'
'HelloWorld'
>>> 'Hello' * 2
'HelloHello'
>>> type('Hello')
<class 'str'>
>>> str(2 + 2)
'4'
>>> str(2 + 2) * int('2' + '2')
'4444444444444444444444'
>>> s = str(2 + 2) * int('2' + '2')
>>> len(s)
22

>>> int('abc')
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    int('abc')
ValueError: invalid literal for int() with base 10: 'abc'
>>> help
Type help() for interactive help, or help(object) for help about object.

>>> help(int)

###Типы значений

'int', 'float', 'str', 'bool'

>>> int(1.5)
1
>>> bool(12)
True
>>> bool(-1)
True
>>> bool(0)
False
>>> bool('hello')
True
>>> bool('World')
True
>>> bool('')
False
>>> True
True
>>> True + False
1
>>> int(True)
1
>>> int(False)
0
>>> s = 'Hello, Word!'
>>> print(s)
Hello, Word!
>>> x = 5
>>> print(x, s)
5 Hello, Word!
>>> s = 'Hello,\nWorld!'
>>> print(s)
Hello,
World!
>>> len(s)
13
>>> s = 'Hello,\tWorld!'
>>> print(s)
Hello,	World!
>>> print('\')
      
SyntaxError: EOL while scanning string literal
>>> print('\\')
\
>>> print('I\'m a student')
I'm a student
>>> print("I'm a student")
I'm a student
>>> s
'Hello,\tWorld!'
>>> x
5
>>> type(x)
<class 'int'>
>>> y = 10
>>> z = 20
>>> print(x, y, z)
5 10 20
>>> print(x, ':', y, ':', z)
5 : 10 : 20
>>> help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

>>> print(x, ':', y, ':', z, sep = ' : ')
5 : : : 10 : : : 20
>>> print(x, y, z, sep = ' : ')
5 : 10 : 20
>>> print(x, y, z, sep = ':')
5:10:20
>>> print("%2d:%2d:%2d" % (x, y, z))
 5:10:20
>>> print("%02d:%02d:%02d" % (x, y, z))
05:10:20
>>> y = 2
>>> print("%02d:%02d:%02d" % (x, y, z))
05:02:20
>>> name = input()
Вася Баранов
>>> name
'Вася Баранов'
>>> age = input()
17
>>> type(age)
<class 'str'>
>>> age = int(age)
>>> type(age)
<class 'int'>

>>> import math
>>> math
<module 'math' (built-in)>
>>> math.sin(math.pi/2)
1.0
>>> math.sin(math.pi/4)
0.7071067811865475
>>> 2  ** 0.5 / 2
0.7071067811865476
>>> 3 ** 3 ** 3
7625597484987
>>> 3 ** 27
7625597484987
>>> 3 ** 3 ** 3 == 3 ** 27
True
>>> 2 ** 5 <= 3 ** 3
False
>>> 2 + 2 != 5

###Код
print('Как тебя зовут?')
name = input()
print('Рад познакомится, ', name, '!', sep = '')
age = int(input('Сколько тебе лет, ' + name + '?'))
print('А я думал, тебе', age + 1, end = '')
x = age + 1
if x >= 11 and x <= 19:
    print(' лет')
elif x % 10 == 1:
    print(' год')
elif x % 10 >= 2 and x % 10 <= 4:
    print(' года')
else:
    print(' лет')
print('!..')
