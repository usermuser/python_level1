import os, sys
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# print(os.listdir())

# os.mkdir(path, mode)
# try:
#     os.mkdir('dirname')
# except FileExistsError:
#     print('dirname exists')


def show_dirs():
    dirs_list = []
    for item in os.scandir():
        if item.is_dir():
            # print(item.name)
            dirs_list.append(item.name)
    return dirs_list


print('Данный скрипт запущен из директории:\n', os.getcwd())
# print('\nСписок директорий в текущей директории:\n')

dirs_lst = show_dirs()
print('\nСписок директорий в текущей директории\n', dirs_lst)
try:
    os.rmdir()
except OSError:
    print('Директория не пустая')
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