"""
Напишите игру "Крестики-нолики".
"""
from random import randint

def print_board(list):
    print('-' * 13)
    for el in list:
        print('|', end=' ')
        print(*el, sep=' | ', end=' | \n')
        print('-' * 13)

def check(list):
    if list[0][0] == list[0][1] == list[0][-1] != ' ':
        return 1
    elif list[1][0] == list[1][1] == list[1][-1] != ' ':
        return 1
    elif list[-1][0] == list[-1][1] == list[-1][-1] != ' ':
        return 1
    elif list[0][0] == list[1][0] == list[-1][0] != ' ':
        return 1
    elif list[0][1] == list[1][1] == list[-1][1] != ' ':
        return 1
    elif list[0][-1] == list[1][-1] == list[-1][-1] != ' ':
        return 1
    elif list[0][0] == list[1][1] == list[-1][-1] != ' ':
        return 1
    elif list[0][-1] == list[1][1] == list[-1][0] != ' ':
        return 1
    else:
        return 0

if __name__ == '__main__':
    lst = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

print('КРЕСТИКИ-НОЛИКИ')
print_board(lst)

players = ['O', 'X']
turn = randint(0, 1)
player = players[turn]

while True:
    print(f'Укажите расположение {player}: строку и столбец через пробел.')
    row, col = [int(i) for i in input().split()]
    lst[row][col] = player
    c = check(lst)
    if c == 1:
        print('Победил ', player)
        break
    else:
        turn = not turn
        player = players[turn]
        print_board(lst)
