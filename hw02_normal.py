from random import randint
# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

print('Задача-1. Первый вариант')
from math import sqrt

list1 = [2, -5, 8, 9, -25, 25, 4]
right_result = [3, 5, 2]
result = []

for item in list1:
    if item > 0 and sqrt(item).is_integer():
        result.append(int(sqrt(item)))
print('Expected', right_result, ', got',result)

if right_result == result:
    print('Test OK')
else:
    print('Test Failed')

print('\nЗадача-1. Второй вариант')
result = [int(sqrt(item)) for item in list1 if item > 0 and sqrt(item).is_integer()]
print('Expected', right_result, ', got',result)

if right_result == result:
    print('Test OK')
else:
    print('Test Failed')

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)
print('\nЗадача-2')
        #input = string
        #output = string
days = {'01':'первое', '02':'второе', '03':'третье'}      # и так далее
months ={'09':'сентября', '10':'октября', '11':'ноября'}  # и так далее
input = '02.11.2013'
correct_output = 'второе ноября 2013 года.'
input_list = input.split('.')

day = days[input_list[0]]      # по ключю берем значение из словаря days
month = months[input_list[1]]  # аналогично из months
year = input_list[2]

output ='{} {} {} года.'.format(day, month, year)
print('Входные данные:', input)
print('Ожидаем:', correct_output)
print('Получили:', output)

if output == correct_output:
    print('Test OK')
else:
    print('Test Failed')

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

print('\nЗадача-3. Первый вариант')
n = 10
lst1 = []
    # input type = int
    # output type = list
for i in range(n):
    lst1.append(randint(-100,100))
print(lst1)

print('\nЗадача-3. Второй вариант')
lst2 = [randint(-100,100) for x in range(n)]
print(lst2)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

print('\nЗадача-4. Вариант А')
lst1 = [1, 2, 4, 5, 6, 2, 5, 2]
lst2 = [1, 2, 4, 5, 6]
lst1 = list(set(lst1))            # забавная тавтология
print('expected:', lst2)
print('got: ', lst1)

if lst1 == lst2:
    print('Test OK')
else:
    print('Test Failed')


print('\nЗадача-4. Вариант Б')
lst1 = [1, 2, 4, 5, 6, 2, 5, 2]
correct_lst = [1, 4, 6]

my_lst = []
for i in lst1:
    if lst1.count(i) == 1:
        my_lst.append(i)

print("expected:", correct_lst)
print("got: ", my_lst)

if my_lst == correct_lst:
    print('Test OK')
else:
    print('Test Failed')

