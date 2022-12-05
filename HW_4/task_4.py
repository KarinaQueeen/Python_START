"""
Даны файлы, в каждом из которых находится запись многочлена.
Найти сумму многочленов из файлов, ввести в консоль и записать в файл.
Входными данными для этой задачи являются выходные данные их предыдущей.

Ввод: значения типа <str>, полученные из файлов.
Вывод: значение типа <str>, файл с одной строкой.

Примеры:
9x^5+7x^4+7x^3+9x^2+6x+17=0
3x^2+2x+1=0
9x^5+7x^4+7x^3+12x^2+8x+18=0
"""
new_list = []
data = open('HW_4_task_3.txt')
for el in data:
    new_list.append(el)
data.close()
new_list = [l for l in new_list if l != '\n']

abc1 = new_list[0].split(' + ')
a = abc1[-1].split(' = ')
abc1[-1] = a[0]
abc2 = new_list[1].split(' + ')
a = abc2[-1].split(' = ')
abc2[-1] = a[0]

for i in abc2:
    abc1.append('-' + i)

polynomial = []

for p in abc1:
    polynomial.append(p)
    polynomial.append(' + ')
polynomial[-1] = ' = 0'   # все до чего я смогла додуматься :)

print(polynomial)
data = open('HW_4_task_4.txt', 'a', )
data.writelines(polynomial)
data.writelines("\n")
data.close()
