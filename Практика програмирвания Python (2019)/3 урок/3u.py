Для лучшего запоминания материала: повторить через час, день, неделю, месяц, год.

###Графика по Управление клавишами.
kpolyakov.spb.ru - сайт с проектом по Graph и многое другое.

###Списки (list) и кортежи (tuple) в Python

A = [1, 2, '3', True, 5, (30, 40), [50, 60]] #список внутри которого есть кортеж и список
C = (1, "Hello", 3) #кортеж
Кортеж не изменяемый объект!
B = A #ссылка на объект A
B = list(A) #создание копии объекта
B = A.copy() #создание копии объекта
Доступ по ссылке начинается с 0, тоесть индексы начинаются с 0.
B[0] = 10
print(A) #[10, 2, '3', True, 5, (30, 40), [50, 60]]

x = 10
x = int('AB', base = 16) #AB - цифра в шестнадцатеричной системе

import array #библиотека массивы в Python, но списки лучше!

A = [1, 2, 3]
A.append(4) #Добавление в конец списка объекта

x = 2
y = x
print(x is y) #True

A = list(range(1, 100, 1))
B = []
for i in range(len(A)):
	if A[i] % 7 == 0:
		B.append(A[i])
Тоже самое только легче:
B = [x for x in A if x % 7 == 0]

B = (x * 2 for x in A if x % 7 == 0)
После создания нельзя изменить!