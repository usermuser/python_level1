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
        self._card = Card().create_card()
        # self.card = copy.deepcopy(self.card_init)
        self._card_name = '------ Ваша карточка -----'
        # print('Player instance')
        # print(self.card)

    def show_card(self):
        print(self._card_name)
        line_len = len(self._card_name)
        for i in self._card:
            print(' '.join(i).rjust(line_len, ' '))
        print('--------------------------')


class Cpu(Person):
    def __init__(self):
        self._card = Card().create_card()
        # self.card = copy.deepcopy(self.card_init)
        self._card_name = '-- Карточка компьютера ---'
        # print('Cpu instance')

    def show_card(self):
        print(self._card_name)
        line_len = len(self._card_name)
        for i in self._card:
            print(' '.join(i).rjust(line_len, ' '))
        print('--------------------------')


class Bag():
    def __init__(self):
        self._barrels = [x for x in range(1, 91)]

    def _bag(self):
        while len(self._barrels):
            barrel = self._barrels.pop(random.randrange(len(self._barrels)))
            yield barrel

    def get_barrel(self):
        return next(self._bag())


class Game():
    def __init__(self, player, cpu, bag):
        self.player = player
        self.cpu = cpu
        self.bag = bag


    def start(self):
        exit = False

        while not exit:
            _barrel = bag.get_barrel()
            print('Выпал бочонок', _barrel)

            self.player.show_card()
            self.cpu.show_card()

            _answer = self.ask()
            barrel_in_card = self.check_ok(_barrel)

            if _answer and barrel_in_card:
                self.player._card[self.player._card.index(_barrel)] = '-'

            elif _answer and not barrel_in_card:
                print('В твоей карточке нет такого номера!')
                exit = True






    def check_ok(self, _barrel):
        if _barrel in self.player._card:
            return True
        else:
            return False

    def ask(self):
        ask_exit = False
        while not ask_exit:
            answer = int(input('Что вы хотите сделать?\n'
                           'Нажмите 1 если хотите зачеркнуть\n'
                           'Нажмите 2 если хотите продолжить\n'
                            'Нажмите 3 для выхода'))
            if answer == 3:
                ask_exit = True
            elif answer == 1:
                return True
            elif answer == 2:
                return False
            else:
                print('Вы ввели что-то не то')







if __name__ == '__main__':

    player = Player()
    cpu = Cpu()
    bag = Bag()

    # player.show_card()
    # cpu.show_card()



    game = Game(player, cpu, bag)
    game.start()
