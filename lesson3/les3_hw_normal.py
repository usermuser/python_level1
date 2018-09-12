# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000


names = ['Денис', 'Сергей', 'Владимир', 'Гвидо']
salaries = ['100500.00', '15000', '100', '654321.321']

person_card = dict(zip(names, salaries))
print('person card =', person_card)

with open('salary.txt', 'w', encoding='utf-8') as file:
    for name, salary in person_card.items():
        print(name, salary)
        file.write('{} - {}\n'.format(name, salary))

print('Конец первой части. Файл записан.')


# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко,
# используя возможности языка Python.

# def lst_to_dict(*args):
#     dict={}
#     print('*args', args)
#     for item in args:
#         item = item.split('-')
#         dict.update({item[0]:item[1].strip()})
#     return dict
#
# print('\nВторая часть задачи\n')
# with open('salary.txt', 'r', encoding='utf-8') as file:
#     data_list = file.readlines()
#     print('data_list = ', data_list)
#     result = map(lst_to_dict, data_list)
#     result_list = list(result)
#     print(result_list)
#     print('\nКонец второй части.')
'''
with open('salary.txt', 'r', encoding='utf-8') as file:
    dict = {}
    print('marker')
    for line in file.readlines():
        key, val = line.strip().split('-')
        dict[key] = val
'''

with open('salary.txt', 'r', encoding='utf-8') as file:
    dict1 = {}
    print('Посчитаем зарплату минус 13%')
    for line in file.readlines():
        key, val = line.strip().split('-')
        dict1[key] = float(val)
        dict1[key] -= dict1[key]*0.13
    print(dict1, end='\n')

print('Уберем людей получающих зп больше 50000')

filtered_dict = filter(lambda x: x < 50000, dict1.values())
print(list(filtered_dict))




