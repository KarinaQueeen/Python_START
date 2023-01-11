# МОДУЛЬ РАБОТЫ С ДАННЫМИ
from logger import log
import view


def get_data() -> list:
    ''' ВЫГРУЗКА ДАННЫХ '''

    with open('data_HW7.csv', encoding= 'UTF-8') as data:
        new_list = data.readline()
        view.print_book(new_list)


@log
def add_data(data: list):
    ''' ДОБАВЛЕНИЕ ДАННЫХ '''

    book = view.input_data()
    with open('data_HW7.csv', 'w', encoding= 'UTF-8') as data:
        data.write(data)
