"""
Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
Результат округлить до сотых.

Ввод: четыре значения типа <int>
Вывод: значение типа <float>

Пример:

4 10
11 5
9.22
"""
import math

print('Введите координаты точек')
a = int(input('x1 = '))
b = int(input('y1 = '))
c = int(input('x2 = '))
d = int(input('y2 = '))

e = abs(math.sqrt((c - a) ** 2 + (d - b) ** 2))
print(f'Расстояние между точками ({a};{b}) и ({c};{d}) равно {round(e, 2)}')