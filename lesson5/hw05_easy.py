import os, sys
import time
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# print(os.listdir())

# os.mkdir(path, mode)

dirname_prefix = 'dir_'

# с помощью генератора списков создадим список имен директорий, которые нужно создать
dirs_to_create = [dirname_prefix + str(i) for i in range(1,10)]
print('Директории с этими именами мы будем создавать:', dirs_to_create)

def create_dirs(*args):
    for dir in args:
        try:
            os.mkdir(dir)
        except FileExistsError:
            print('Директория с именем {} уже существует'.format(dir))

def remove_dirs(*args):
    for dir in args:
        try:
            os.rmdir(dir)
        except OSError:
            print('Директория с именем {} не пустая'.format(dir))


def show_dirs():
    dirs_list = []
    for item in os.scandir():
        if item.is_dir():
            dirs_list.append(item.name)
            dirs_list.sort()
    return dirs_list

print('\nДанный скрипт запущен из директории:\n', os.getcwd())

print('\nСписок директорий в текущей директории ДО создания наших директорий:\n', show_dirs())

create_dirs(*dirs_to_create)

print('\nСписок директорий в текущей директории ПОСЛЕ создания наших директорий:\n', show_dirs())


# try:
#     os.rmdir(os.getcwd)
# except OSError:
#     print('Директория не пустая')
# def remove_dirs(*args):
#     for dir in args:
#         print(dir)
#         # os.remove(dir)
#
# print('удалим директории:', remove_dirs(dirs_lst))

# for path in sys.path:
#     print(path)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.