import os, sys
import time

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

dirname_prefix = 'dir_'

# с помощью генератора списков создадим список имен директорий, которые нужно создать
dirs_to_create = [dirname_prefix + str(i) for i in range(1, 10)]


def create_dirs(*args):
    for dir in args:
        try:
            os.mkdir(dir)
        except FileExistsError:
            print('Директория с именем {} уже существует'.format(dir))


def remove_dirs(*args):  # папки на удаление можно передавать списком
    removed_dirs = []
    for dir in args:
        try:
            os.rmdir(dir)
            removed_dirs.append(dir)
        except OSError:
            print('Директория с именем {} не пустая'.format(dir))

    print('Список оставшихся директорий после удаления:\n', show_dirs())
    # список удаленных директорий будем хранить в removed_dirs на всякий случай
    removed_dirs.sort()

def show_dirs():
    dirs_list = []
    for item in os.scandir():
        if item.is_dir():
            dirs_list.append(item.name)
            dirs_list.sort()
    # print(dirs_list)
    return dirs_list


def show_dirs_and_files():  # эту функцию создал для следующего задания
    dirs_list = []
    for item in os.scandir():
        dirs_list.append(item.name)
        dirs_list.sort()
    return dirs_list


if __name__ == '__main__':
    print('\nЗадача-1.')
    print('Директории с этими именами мы будем создавать:', dirs_to_create)
    print('\nДанный скрипт запущен из директории:\n', os.getcwd())

    print('\nСписок директорий в текущей директории ДО создания наших директорий:\n', show_dirs())

    create_dirs(*dirs_to_create)  # пытаемся создать директории

    print('\nСписок директорий в текущей директории ПОСЛЕ создания наших директорий:\n', show_dirs())

    print('\nТеперь удалим созданные директории.')
    dirs_to_remove = dirs_to_create
    remove_dirs(*dirs_to_remove)  # пытаемся удалить пустые директории

    # Задача-2:
    # Напишите скрипт, отображающий папки текущей директории.
    print('\nЗадача-2.')
    print('Текущая директория:', os.getcwd())
    print('Список папок в текущей директории:', show_dirs())
