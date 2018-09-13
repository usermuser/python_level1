# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.
player = {'name': 'Barbaz', 'health': 95, 'damage': 5, 'armor': 1.2}
enemy = {'name': 'Spammer', 'health': 90, 'damage': 7, 'armor': 1.2}

# print('player = ', player)
# print('enemy = ', enemy)

def attack(attacker, victim):
    print('Игрок ', attacker['name'], 'атаковал', victim['name'], 'с атакой', attacker['damage'], 'хп было', victim['health'])
    dmg = dmg_calc(attacker['damage'], victim['armor'])
    # print("стало {} - {} = ".format(victim['health'], dmg ), end='')
    victim['health'] -= dmg
    print('с учетом брони хп стало ', victim['health'])

def dmg_calc(damage=1, armor=1.2):
    # dealt_dmg = damage / armor
    dealt_dmg = damage / armor
    return dealt_dmg

def save_to_file(**kwargs):
    filename = kwargs['name']
    filename = filename + '.txt'
    print(filename)
    with open(filename, 'w', encoding='utf-8') as file:
        for key, value in kwargs.items():
            file.write('{} - {}\n'.format(key, value))

def readfile(**kwargs):
    char = {}
    filename = kwargs['name'] + '.txt'
    with open(filename, 'r', encoding='utf-8') as file:
        for key, value  in kwargs.items():
            char[key] = value
        return char

save_to_file(**player)
save_to_file(**enemy)

player = readfile(**player)
enemy = readfile(**enemy)

def fight(player, enemy):
    turn = 1
    while player['health'] > 0 or enemy['health'] > 0:
        if turn == 1:
            attack(player, enemy)
            turn = 2
        else:
            attack(enemy, player)
            turn = 1

fight(player, enemy)
# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
## после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.
