import os, sys
import time

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
print('\nЗадача-1.')
dirname_prefix = 'dir_'

# с помощью генератора списков создадим список имен директорий, которые нужно создать
dirs_to_create = [dirname_prefix + str(i) for i in range(1, 10)]
print('Директории с этими именами мы будем создавать:', dirs_to_create)


def create_dirs(*args):
    for dir in args:
        try:
            os.mkdir(dir)
        except FileExistsError:
            print('Директория с именем {} уже существует'.format(dir))


def remove_dirs(*args):
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
    return dirs_list


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

def show_dirs():
    dirs_list = []
    for item in os.scandir():
        if item.is_dir():
            dirs_list.append(item.name)
            dirs_list.sort()
    print(dirs_list)

print('Текущая директория:', os.getcwd())
print('Список папок в текущей директории:')
show_dirs()





# print(os.listdir())

# for path in sys.path:
#     print(path)