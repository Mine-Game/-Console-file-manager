import random


def game2():
    user_number = input('Введите число от 1 до 100 или запишите его на листочке, я '
                        'буду отгадывать ваше число, если записали на листе, введите 0: ')

    is_winner = False

    min_number = 1
    max_number = 100


    while not is_winner:
        number = random.randint(min_number, max_number)
        Player_Answer = input(f'Вы загадали число {number}, введите "Да", если я угадал, введите "<", если нужно меньше или знак ">", в обратном случае: ')
        if Player_Answer == 'Да':
            print('Я так и знал, спасибо за игру :)')
            is_winner = True
        elif Player_Answer == '>':
            min_number = number + 1
        elif Player_Answer == '<':
            max_number = number - 1

if __name__ == '__main__':
    game2()