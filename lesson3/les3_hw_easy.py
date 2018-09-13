# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

print('\nЗадание - 1.')


def my_func(name, age, city):
    output = '{}, {} года(а), проживает в городе {}'.format(name, age, city)
    print(output)
    return output


name = input('Введите свое имя: ')
name = name.title()
age = int(input('Введите свой возраст: '))
city = input('Введите свой город: ')

my_func(name, age, city)

# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

print('\nЗадание - 2.')


def get_max(a, b, c):
    maxnum = a
    if b > a:
        maxnum = b

    if c > maxnum:
        maxnum = c

    print('Наибольшее из {},{},{} ='.format(a, b, c), maxnum)
    return maxnum


# Проверим все комбинации
get_max(1, 2, 3)
get_max(1, 3, 2)
get_max(2, 3, 1)
get_max(3, 2, 1)
get_max(3, 1, 2)

# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов


print('\nЗадание - 3-1. Количество строковых аргументов неизвестно')


def arg_len(*args):
    biggest_word = ''
    for word in args:
        if len(word) > len(biggest_word):
            biggest_word = word
    print(biggest_word)
    return biggest_word


biggest = arg_len('абвddddf dsfdfa', 'абвгд', 'ноутбук')
print(biggest)

print('\nЗадание - 3-2. Количество известно')

# передадим известное количество аргументов в виде списка
# потренируемся разворачивать список

words = ['ppapapa', 'fooo', 'bar', 'bazzzzzzzzzzzzz']
lst = arg_len(*words)
print(lst)
