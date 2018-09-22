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
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.damage = self.generate_damage()
        self.armor = self.generate_armor()

    def generate_armor(self):
        self.armor = random.randint(1, 5)
        return self.armor

    def generate_damage(self):
        self.damage = random.randint(5, 15)
        return self.damage

    def _calculate_damage(self, armor):
        return self.damage // armor

    def attack(self, victim):
        damage = self._calculate_damage(victim.armor)
        victim.health -= damage
        print('{} нанес {} урона,'
              ' у {} осталось {} жизней '.format(self.name, damage, victim.name, victim.health))

class Player(Person):

    def battle_cry(self):
        return 'Boom shaka laka!'


class Enemy(Person):

    def battle_cry(self):
        return 'Slamma jamma!'

class Game():
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    # позволим рандому определить того, кто будет ходить первым
    def first_move(self, player1_name, player2_name):
        tmp = [player1_name, player2_name]
        return random.choice(tmp)

    # игроки по-очереди атакуют друг-друга
    def start_game(self):
        attacker = self.first_move(self.player.name, self.enemy.name)
        while player.health > 0 and enemy.health > 0:

            if attacker == player.name:
                player.attack(enemy)    # игрок player атакует игрока enemy
                attacker = enemy.name
            else:
                enemy.attack(player)    # игорок enemy атакует игрока player
                attacker = player.name

        # определение победителя
        if player.health > 0:
            print(player.name, 'с криком {} победил!'.format(player.battle_cry()))
        else:
            print(enemy.name, 'с криком {} победил!'.format(enemy.battle_cry()))


if __name__ == '__main__':

    player = Player('Крушила')
    enemy = Enemy('Шустрик', 120 )
    new_game = Game(player, enemy)
    new_game.start_game()
