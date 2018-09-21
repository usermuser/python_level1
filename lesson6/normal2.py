import random
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

    def _calculate_damage(self, damage, armor):
        return damage // armor

    def attack(self, victim):
        damage = self._calculate_damage(self.damage, victim.armor)
        victim.health -= damage
        print('{} нанес {} урона,'
              ' у {} осталось {} жизней '.format(self.name, damage, victim.name, victim.health))

class Player(Person):

    def battle_cry(self):
        return 'Boom shaka laka!'


class Enemy(Person):

    def battle_cry(self):

        return 'Slamma jamma!'


def start_game():
    attacker = enemy
    while player.health > 0 and enemy.health > 0:
        if attacker == player:
            player.attack(enemy)
            attacker = enemy
        else:
            enemy.attack(player)
            attacker = player

    if player.health > 0:
        print(player.name, 'с криком {} победил!'.format(player.battle_cry()))
    else:
        print(enemy.name, 'победил!')


player = Player('Крушила', random.randint(50, 150), random.randint(5, 15), random.randint(1, 5))
enemy = Enemy('Шустрик', random.randint(50, 150), random.randint(5, 15), random.randint(1, 5))

start_game()
