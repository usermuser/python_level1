import os

import lesson5.hw05_easy as lib

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
print('Вы находитесь в директории', os.getcwd())
lib.create_dirs('2')
def start():
    while True:
        choice = int(input('\nВыберите пункт:\n'
                           '1. Перейти в папку\n'
                           '2. Просмотреть содержимое текущей папки\n'
                           '3. Удалить папку\n'
                           '4. Создать папку\n'
                           '5. Выход\n'
                           '------------------------\n'
                           'Ваш выбор:'))
        if choice == 5:
            break
        else:
            process_user_choice(choice)

def process_user_choice(choice):
    if choice == 1:
        print('Доступные папки\n', lib.show_dirs())
        dir = input('\nВведите название папки: ')
        try:
            os.chdir(dir)
        except FileNotFoundError:
            print('\nТакой папки не существует\n')

    elif choice == 2:
        if not lib.show_dirs_and_files(): # если функция вернула пустой список файлов и папок
            print('В этой папке пусто')
        else:
            print(lib.show_dirs_and_files())

    elif choice == 3:
        dir = input('\nВведите название папки: ')
        lib.remove_dirs(dir)

    elif choice == 4:
        dir = input('\nВведите название папки: ')
        lib.create_dirs(dir)
        print('Папка {} создана'.format(dir))

start()
# def change_dir(dirname):
#     os.chdir('1')
