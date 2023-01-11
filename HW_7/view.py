# МОДУЛЬ ОТОБРАЖЕНИЯ

from logger import log
from random import randint


@log
def greetings():
    ''' ПРИВЕТСТВИЕ '''

    print('Справочник запущен!')


@log
def menu() -> str:
    ''' ВЫБОР ДЕЙСТВИЯ '''

    return int(input('Меню:\n'
                 '1 - отобразить справочник\n'
                 '2 - добавить запись\n'
                 '3 - выход\n'
                 'Выберите действие: '))


@log
def print_book(data: list):
    '''ВЫВОД ДАННЫХ'''

    if data:
        for el in data:
            print(f"ID: {el['id']} | Имя: {el['name']} | Фамилия: {el['surmame']} | Дата рождения: {el['birsdate']} | Место работы: {el['work']} | Телефон: {el['telephone']}")
    else:
        print('Нет данных для отображения...')


@log
def input_data():
    '''ПРИЕМ ДАННЫХ'''

    book == {}
    book['id'] = randint(1, 100)
    book['name'] = input('Введите имя: ')
    book['surname'] = input('Введите фамилию: ')
    book['birsdate'] = input('Добавьте дату рождения: ')
    book['work'] = input('Укажите место работы: ')
    book['telephone'] = input('Запишите номер телефона: ')
