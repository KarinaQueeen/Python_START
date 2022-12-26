"""
Реализуйте RLE алгоритм шифрования строки: замените повторяющиеся символы строки на один символ и число его повторов.
На первом месте идет количество повторов, на втором сам символ.
Восстановите строку после шифрования.

Ввод: значения типа <str>, можно получить из файла.
Вывод: значение типа <str>, можно записать в файл.

Примеры:

5ы5р3 6а8г
"""
def coding(line):
    code = ''
    count = 1
    symbol = ''

    for s in line:
        if s != symbol:
            if symbol:
                code += str(count) + symbol
            count = 1
            symbol = s
        else:
            if count == 9:
                code += str(count) + symbol
                count = 1
            count += 1
    return code


def decoding(code):
    decode = ''
    for i in range(0, len(code), 2):
        count, simbol = code[i: i + 1]
        decode += simbol * int(count)
    return decode

line = input('Введите строку для шифрования: ')
code = coding(line)

print(code)
print(decoding(code))
