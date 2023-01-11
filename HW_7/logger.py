# МОДУЛЬ ЛОГГИРОВАРИЯ

from datetime import datetime


def log(func):
    ''' ЛОГГИРОВАНИЕ '''
    
    def wrapper(*args):
        with open('HW7_log.csv', 'a', encoding= 'UTF-8') as data:
            data.write(
                f'{datetime.now()} ; {func.__name__} ; {func.__doc__}\n')
        return func(*args)
    return wrapper
