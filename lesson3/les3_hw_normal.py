# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000

# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко,
# используя возможности языка Python.


tax = 13  # Текущий налог в стране
names = ['Денис', 'Сергей', 'Владимир', 'Гвидо']
salaries = ['100500.00', '15000', '100', '654321.321']


# открывает указанный файл и записывает в него словарь любой длины
def write_dict_to_file(file, **kwargs):
    with open(file, 'w', encoding='utf-8') as file:
        for name, salary in kwargs.items():
            # print(name, salary)
            file.write('{} - {}\n'.format(name, salary))


# открывает указанный файл и читает его
# и вычитает заданное количество процентов
# но перед этим все значения преобразуем в float
# если у Владимира 87.0 значит функция считает правильно
def tax_cutter(filename, percent):
    with open(filename, 'r', encoding='utf-8') as file:
        temp_dict = {}
        for line in file.readlines():
            key, val = line.strip().split('-')
            temp_dict[key] = float(val)
            temp_dict[key] -= temp_dict[key] * (percent / 100)
        # print(temp_dict, end='\n')
    return temp_dict


# фильтрует словарь по заданному значению
def filt_dict_values_by_setpoint(setpoint=50, **kwargs):
    temp_dict = {}                    # сюда положим отфильтрованное
    for k, v in kwargs.items():
        if v < setpoint:
            temp_dict[k] = v
    # print(temp_dict)
    return temp_dict


# делает имя КАПСОМ
def capser(**kwargs):
    temp_dict = {}
    for k,v in kwargs.items():
        k = k.upper()
        temp_dict[k] = v
    print(temp_dict)
    return temp_dict


# создадим словарь c зарплатами
person_card = dict(zip(names, salaries))

# запишем в файл
write_dict_to_file('salary.txt', **person_card)

# прочитаем файл и вычтем налоги
salary_after_tax = tax_cutter('salary.txt', tax)

# отфильтруем тех, кто получает больше 50000
filtered_salary = filt_dict_values_by_setpoint(50000, **salary_after_tax)

# Сделаем имена в верхнем регистре
capser(**filtered_salary)
