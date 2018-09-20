import os
import sys
# rmdir or remove
try:
    import lesson5.hw05_easy_3 as my_lib
    import lesson5.hw05_easy as my_lib2
except ImportError:
    import hw05_easy_3 as my_lib
    import hw05_easy as my_lib2

# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создать копию файла")
    print("rm <dir_name> - удалить пустую папку или файл")
    print("cd <full_path or relative_path> - меняет текущую папку на указанную")
    print("ls - отображение полного пути текущей директории")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")

def copy_file():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    file_path = os.path.join(os.getcwd(), file_name)
    try:
        my_lib.copy_file(file_name)
        print('Файл с именем copy_{} успешно создан'.format(file_name))
    except FileNotFoundError:
        print('Файла с именем {} не существует'.format(file_name))

def remove_file_or_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return

    confirm = input('Вы уверены что хотите удалить {}? (Y/N)'.format(dir_name))
    if confirm == 'Y':
        dir_path = os.path.join(os.getcwd(), dir_name)
        print(dir_name, '\n', dir_path)
        if os.path.isdir(dir_path):
            try:
                os.rmdir(dir_path)
                print('Директория {} удалена'.format(dir_name))
            except OSError:
                print('Директория с именем {} не пустая'.format(dir_name))
        else:
            try:
                os.remove(dir_path)
                print('Файл {} удален.'.format(dir_name))
            except FileExistsError:
                print('Такого файла нет')

    elif confirm == 'N':
        print('Удаление {} было отменено.'.format(dir_name))

def ls():
    print('\nПолный путь текущей директории:')
    print(os.getcwd())
    print('\nСписок папок и файлов текущей директории:\n', my_lib2.show_dirs_and_files())


def cd():
    if not dir_name:
        print('\nНеобходимо указать имя директории вторым параметром')
        return
    os.chdir(dir_name)
    print('\nВы перешли в директорию {}'.format(dir_name))
    print('Полный путь:', os.getcwd())

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy_file,
    "rm": remove_file_or_dir,
    "cd": cd,
    "ls": ls,
}

if __name__ == '__main__':
    try:
        dir_name = sys.argv[2]
    except IndexError:
        dir_name = None

    try:
        file_name = sys.argv[2]
    except IndexError:
        file_name = None

    try:
        key = sys.argv[1]
    except IndexError:
        key = None


    if key:
        if do.get(key):
            do[key]()
        else:
            print("Задан неверный ключ")
            print("Укажите ключ help для получения справки")
