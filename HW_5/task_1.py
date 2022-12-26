"""
Напишите программу, удаляющую из текста все слова, в которых присутствуют буквы «а», «б» и «в».

Ввод: значение типа <str>
Вывод: значение типа <str>
"""

text = input('Введите текст:\n').lower().split()

def del_word_1(text):
    return ' '.join(el for el in text if not ('а' in el and 'б' in el and 'в' in el))


def del_word_2(text):
    return ' '.join(filter(lambda x: not ('а' in x and 'б' in x and 'в' in x), text))

print(del_word_1(text))
print(del_word_2(text))