"""
Задайте список случайных чисел. Выведите список чисел, которые не повторяются в заданном списке.

Ввод: значение типа <list> (либо значения типа <int> – размерность списка)
Вывод: значение типа <list>

Пример:
[1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9]
[2, 4, 6, 8]
"""
import random
new_list = [str(random.randint(1, 9))
            for r in range(int(input('Введите размер списка: ')))]
clean_list = []
for i in range(len(new_list)):
    if (new_list).count(new_list[i]) <= 1:
        clean_list.append(new_list[i])
new_list = [int(el) for el in new_list]
print(new_list)
clean_list = [int(elem) for elem in clean_list]
print(clean_list)
