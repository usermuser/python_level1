import random
import copy


class ThreeRowsCard():
    def __init__(self, nums_in_row=5):
        self._rows_qty = 3
        self.nums_in_row = nums_in_row


class Card(ThreeRowsCard):
    def __init__(self):
        super().__init__()
        # список случайных номеров для карточки
        self.nums_for_card = random.sample(range(1, 90), 15)
        # print(self.nums_for_card)

    def _create_line(self):
        output_list = []
        for _ in range(self.nums_in_row):
            num = random.choice(self.nums_for_card)
            output_list.append(str(num))
            output_list.sort()
            self.nums_for_card.remove(num)

        # вставим пробелы в рандомные позиции
        for _ in range(4):  # 4 пробела
            output_list.insert(random.randrange(len(output_list)), ' ')
        return output_list

    def create_card(self):
        output = []
        for _ in range(self._rows_qty):
            output.append(self._create_line())
        return output


class Person():
    pass


class Player(Person):
    def __init__(self):
        self.card = Card().create_card()
        # self.card = copy.deepcopy(self.card_init)
        self._card_name = '------ Ваша карточка -----'
        # print('Player instance')
        # print(self.card)

    def show_card(self):
        print(self._card_name)
        line_len = len(self._card_name)
        for i in self.card:
            print(' '.join(i).rjust(line_len, ' '))
        print('--------------------------')


class Cpu(Person):
    def __init__(self):
        self.card_init = Card().create_card()
        self.card = copy.deepcopy(self.card_init)
        self._card_name = '-- Карточка компьютера ---'
        print('Cpu instance')

    def show_card(self):
        print(self._card_name)
        line_len = len(self._card_name)
        for i in self.card:
            print(' '.join(i).rjust(line_len, ' '))
        print('--------------------------')

class Bag():
    def __init__(self):
        self.barrels = [x for x in range(1, 91)]

    def create_bag(self):
        while len(self.barrels):
            barrel = self.barrels.pop(random.randrange(len(self.barrels)))
            yield barrel

    def next_barrel(self):
        return next(self.create_bag())

class Game():
    def __init__(self, player, cpu):
        self.player = player
        self.cpu = cpu

    def start(self):
        pass


if __name__ == '__main__':

    player = Player()
    player.show_card()

    cpu = Cpu()
    cpu.show_card()

    game = Game(player, cpu)
    game.start()