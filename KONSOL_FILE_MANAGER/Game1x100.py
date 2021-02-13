import random

def game1():
    number = random.randint(1,100)
    user_number = None
    count = 0
    level = int(input('Введите уровень сложности от 1 до 3: '))
    levels = {1: 10, 2: 5, 3: 3}
    max_count = levels[level]


    user_count = int(input('Ведите количество пользователей: '))
    users = []
    for i in range(user_count):
        user_name = input(f'Введите имя пользователя {i + 1}: ')
        users.append(user_name)

    is_winner = False
    winner_name = None


    while not is_winner:
        count += 1
        print(f'Осталось попыток: {levels[level] - count + 1}')
        if count> max_count:
            print(f'Все пользователи проиграли, количество попыток закончилось!Правильный ответ: {number}')
            break
        print(f'Попытка № {count}')
        for user in users:
            print(f'Ход пользователя {user}')
            user_number = int(input('Введите число от 1 до 100: '))
            if user_number == number:
                is_winner = True
                winner_name = user
                break
            elif user_number < number:
                    print('Ваше число меньше загаданного')
            else:
                print('Ваше число больше загаданного')
    else:
        print(f'Поздравляю,{user}, вы победили!')

if __name__ == '__main__':
    game1()
