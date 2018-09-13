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
player = {'name': 'Barbaz', 'health': 95, 'damage': 4, 'armor': 2.2}
enemy = {'name': 'Spammer', 'health': 30, 'damage': 2, 'armor': 1.2}


# вычисляет остаток хп после атаки
# если хп после атаки стало <= 0 то функция вернет 1 (exit = 1), иначе 0 (exit = 0)
def attack(attacker, victim):
    print('\nИгрок ', attacker['name'], 'атаковал', victim['name'], 'с атакой', attacker['damage'], ', хп было',
          victim['health'])
    dmg = dmg_calc(attacker['damage'], victim['armor'])
    victim['health'] -= dmg
    victim['health'] = round(victim['health'], 1)
    if victim['health'] <= 0:
        print('с учетом брони хп стало ', victim['health'], end='\n')
        print(attacker['name'], 'победил, хп осталось', attacker['health'])
        return 1
    else:
        print('с учетом брони хп стало ', victim['health'])
        return 0


# вычисляет наносимый урон
def dmg_calc(damage=1, armor=1.2):
    # dealt_dmg = damage / armor
    dealt_dmg = damage / armor
    return dealt_dmg


# сохраняет характеристики персонажа в файл
def save_to_file(**kwargs):
    filename = kwargs['name']
    filename = filename + '.txt'
    print(filename)
    with open(filename, 'w', encoding='utf-8') as file:
        for key, value in kwargs.items():
            file.write('{} - {}\n'.format(key, value))


# считывает характеристики из файла
def readfile(**kwargs):
    char = {}
    filename = kwargs['name'] + '.txt'
    with open(filename, 'r', encoding='utf-8') as file:
        for key, value in kwargs.items():
            char[key] = value
        return char


save_to_file(**player)
save_to_file(**enemy)

player = readfile(**player)
enemy = readfile(**enemy)


# главный цикл программы
def fight(player, enemy):
    turn = 1  # 1 - ходит player, 2 - ходит enemy
    exit = 0  # условие выхода из программы (exit = 1 выходим)
    while not exit:
        if turn == 1:
            exit = attack(player, enemy)  # если после атаки хп стало <= 0, то бой окончен, выходим (exit = 1)
            turn = 2  # переход хода
        else:
            exit = attack(enemy, player)
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
