"""
Задать натуральное число k.
Сформируйте многочлен (полином) степени k со случайными коэффициентами из промежутка от 0 до 100, включительно.
Многочлен вывести в консоль и записать в файл.

Ввод: значение типа <int>
Вывод: значение типа <str>, файл с одной строкой.

Пример:
2
2x^2 + 4x + 5 = 0
"""
import random
print('Введите степень k для многочлена ax^k + bx + c = 0')
k = input()
polynomial = [str(random.randint(0, 100)), 'x^', k, ' + ',
              str(random.randint(0, 100)), 'x', ' + ', str(random.randint(0, 100)), ' = 0']

if polynomial[0] == '0' and polynomial[4] == '0' and polynomial[7] == '0':
    polynomial = []
elif polynomial[0] == '0' and polynomial[4] == '0' and polynomial[7] != '0':
    polynomial = []
else:
    if k == '0':
        del polynomial[0:4]
        if polynomial[0] != '0' and polynomial[3] == '0':
            polynomial[3] = '1'
        elif polynomial[0] != '0' and polynomial[3] != '0':
            polynomial[3] = str(int(polynomial[3]) + 1)
    elif k == '1':
        if polynomial[0] == '0' and polynomial[3] != '0' and polynomial[7] != '0':
            del polynomial[0:4]
        elif polynomial[0] != '0' and polynomial[3] == '0' and polynomial[7] != '0':
            del polynomial[1:5]
        elif polynomial[0] != '0' and polynomial[3] != '0' and polynomial[7] == '0':
            polynomial[4] = str(int(polynomial[0]) + int(polynomial[4]))
            del polynomial[0:4]
            del polynomial[2:4]
        elif polynomial[0] == '0' and polynomial[3] != '0' and polynomial[7] == '0':
            del polynomial[0:4]
            del polynomial[2:4]
        elif polynomial[0] != '0' and polynomial[3] == '0' and polynomial[7] == '0':
            polynomial[1] = 'x'
            del polynomial[2:8]
    elif int(k) > 1:
        if polynomial[0] == '0' and polynomial[3] != '0' and polynomial[7] != '0':
            del polynomial[0:4]
        elif polynomial[0] != '0' and polynomial[3] == '0' and polynomial[7] != '0':
            del polynomial[3:6]
        elif polynomial[0] != '0' and polynomial[3] != '0' and polynomial[7] == '0':
            del polynomial[6:8]
        elif polynomial[0] == '0' and polynomial[3] != '0' and polynomial[7] == '0':
            del polynomial[0:4]
            del polynomial[2:4]
        elif polynomial[0] != '0' and polynomial[3] == '0' and polynomial[7] == '0':
            del polynomial[3:8]

print(*polynomial)
data = open('HW_4_task_3.txt', 'a', )
data.writelines(polynomial)
data.writelines("\n")
data.close()
