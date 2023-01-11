# СВЯЗЬ МЕЖДУ МОДУЛЯМИ
from logger import log
import model
import view


@log
def start():
    '''СТАРТ'''

    view.greetings()
    while True:
        match view.menu():
            case 1:
                view.print_book(model.get_data())
            case 2:
                model.add_data(view.input_data())
            case 3:
                break
