import sys
from core import create_file, create_folder, get_list, delete_file, copy_file, save_info, change_dir
from Game1x100 import game1
from PcVsPlayergame import game2

save_info('Старт')

command = sys.argv[1]

if command == 'list':
    get_list()
elif command == 'create_file':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсутствует название файла')
    else:
        create_file(name)
elif command == 'create_folder':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсутствует название файла')
    else:
        create_folder(name)
elif command == 'delete':
    try:
        name = sys.argv[2]
    except FileNotFoundError:
        print('Данного файла не существует')
    else:
        delete_file(name)
elif command == 'copy':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсутствует название файла')
    else:
        new_name = sys.argv[3]
        copy_file(name, new_name)
elif command == 'ch':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Необходимо ввести имя папки')
    else:
        change_dir(name)
elif command == 'game1':
    game1()
elif command == 'game1':
    game2()
elif command == 'help':
    print('list - список файлов и папок')
    print('create_file - создание файла')
    print('create_folder - создание папки')
    print('delete - удаление файла или папки')
    print('copy - копирование файла или папки')
    print('game1 - Запуск игры "Угадай число"')
    print('game2 - Запуск игры "Угадай число - наооборот"')

save_info('Конец')