import sys
# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

print('\nЗадача easy-3. Следует запускать из командной строки')

def copy_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        file_content = file.read()
        # print(file_content)

    with open('copy_' + filename, 'w', encoding='utf-8') as file:
        file.write(file_content)

if __name__ == '__main__':
    filename = sys.argv[0]
    copy_file(filename)