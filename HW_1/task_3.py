"""
Напишите программу, которая принимает на вход координаты точки (X и Y) и выдаёт номер четверти плоскости,
в которой находится эта точка (или на какой оси она находится).

Ввод: два значения типа <int>
Вывод: значение типа <int> либо значение типа <str>

Пример:

34
-30
4

2
4
1

-34
0
Точка на отрицательной части оси абсцисс
"""
print('Введите координаты точки')
x = int(input('x = '))
y = int(input('y = '))
if x > 0 and y > 0:
    print('1 четверть')
elif x > 0 and y < 0:
    print('4 четверть')
elif x < 0 and y > 0:
    print('2 четверть')
elif x < 0 and y < 0:
    print('3 четверть')
elif x > 0 and y == 0:
    print('точка на положительной части оси абсцисс')
elif x == 0 and y > 0:
    print('точка на положительной части оси ординат')
elif x == 0 and y < 0:
    print('точка на отрицательной части оси ординат')
elif x < 0 and y == 0:
    print('точка на отрицательной части оси абсцисс')
else:
    print('точка расположена в центре системы координат')
