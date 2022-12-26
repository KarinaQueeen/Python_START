"""
Реализуйте код игры.
Правила игры: на столе лежит N количество конфет. Играют два игрока, делая ход друг после друга.
Первый ход определяется жеребьёвкой, то есть случаен. За один ход можно забрать не более чем k конфет.
Не брать конфеты НЕЛЬЗЯ. Побеждает тот, кто сделал последний ход, то есть забрал со стола остатки конфет.
Он забирает также все конфеты оппонента.
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего оппонента?

a) Добавьте игру против бота
b) Подумайте, как наделить бота простейшим "интеллектом"
"""
from random import randint

sweets = int(input('Введите общее количество конфет: '))
max_sweets = int(input('Укажите максимальное количество конфет за ход: '))

start = sweets % (max_sweets + 1)
#print('Выигрышный первый ход', start)

players = ['Бот', 'Игрок']
turn = randint(0, 1)
player = players[turn]

while True:
    if sweets == max_sweets:
        print()
        print('Победил', player)
        break
    else:
        print('-' * 10)
        print('Ходит', player)
        if player == players[1]:
            g = int(input('Возьмите конфеты: '))
            sweets -= g
            turn = not turn
            player = players[turn]
            if sweets <= max_sweets:
                print()
                print('Победил', player)
                break
            else:
                print('Осталось:', sweets, 'шт')
                f = randint(1, max_sweets)
                print(player, ' взял ', f, 'шт')
                sweets -= f
                turn = not turn
                player = players[turn]
                if sweets <= max_sweets:
                    print()
                    print('Победил', player)
                    break
                print('Осталось:', sweets, 'шт')
        else:
            f = randint(1, max_sweets)
            print(player, ' взял ', f, 'шт')
            sweets -= f
            turn = not turn
            player = players[turn]
            if sweets <= max_sweets:
                print()
                print('Победил', player)
                break
            print('Осталось:', sweets, 'шт')
