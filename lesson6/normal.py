# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

class Person():
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor


class Player(Person):
    pass


class Enemy(Person):
    pass

def attack(attacker, victim):
    damage = calculate_damage(attacker.damage, victim.armor)
    victim.health -= damage
    print('{}')

player = ''
enemy = ''


def start_game():
    while player.health > 0 and enemy.health > 0:
        if attacker = player:
            attack(player, enemy)
            attacker = enemy
        else:
            attack(enemy, player)
            attacker = player

    if player.health > 0:
        print(player.name, 'победил!')
    else:
        print(enemy.name, 'победил!')
