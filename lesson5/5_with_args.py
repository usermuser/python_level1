# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")


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

'''
cp <file_name> - создает копию указанного файла
rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
cd <full_path or relative_path> - меняет текущую директорию на указанную
ls - отображение полного пути текущей директории
'''

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": pass,
    "rm": pass,
    "cd": pass,
    "ls": pass,
}

if __name__ == '__main__':
    try:
        dir_name = sys.argv[2]
    except IndexError:
        dir_name = None

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
