"""
Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек
в этой четверти (x и y).

Ввод: значение типа <int>
Вывод: значение типа <str>

Пример:

3
x < 0, y < 0
"""
print('Введите ночер четверти координат')
num = int(input())
if num == 1:
    print('x > 0, y > 0')
elif num == 2:
    print('x < 0, y > 0')
elif num == 3:
    print('x < 0, y < 0')
elif num == 4:
    print('x > 0, y < 0')
elif num == 0:
    print('x = 0, y = 0')
else:
    print('неверный ввод')
