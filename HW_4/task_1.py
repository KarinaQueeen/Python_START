"""
Выведите список простых множителей натурального числа N.

Ввод: значение типа <int>
Вывод: значение типа <list>

Примеры:
20
[2, 2, 5]

38
[2, 19]
"""

num = int(input('Введите натуральное число: '))
new_list = []

sieve = [el for el in range(num + 1)]
sieve[1] = 0
sieve_list = []
index = 2
while index <= num:
    if sieve[index] != 0:
        sieve_list.append(sieve[index])
        for i in range(0, num + 1, index):
            sieve[i] = 0
    index += 1

while num != 1:
    for k in range(len(sieve_list + 1)):
        if num % sieve_list[k] == 0:
            new_list.append(sieve_list[k])
            num /= sieve_list[k]

print(new_list)
