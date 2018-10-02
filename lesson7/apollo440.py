import random


class ThreeRowsCard():
    def __init__(self, nums_in_row=5):
        self._rows_qty = 3
        self.nums_in_row = nums_in_row


class Card(ThreeRowsCard):
    def __init__(self):
        super().__init__()
        # список случайных номеров для карточки
        self.nums_for_card = random.sample(range(1, 16), 15)

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
        self._card_name = '------ Ваша карточка -----'

    def show_card(self):
        print(self._card_name)
        line_len = len(self._card_name)
        for i in self._card:
            print(' '.join(i).rjust(line_len, ' '))
        print('--------------------------')


class Cpu(Person):
    def __init__(self):
        self._card = Card().create_card()
        self._card_name = '-- Карточка компьютера ---'

    def show_card(self):
        print(self._card_name)
        line_len = len(self._card_name)
        for i in self._card:
            print(' '.join(i).rjust(line_len, ' '))
        print('--------------------------')


class Bag():
    def __init__(self):
        self._barrels = [x for x in range(1, 18)]

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
        self.exit = False
        self._barrel = ''


    def start(self):

        while not self.exit:
            self._barrel = str(bag.get_barrel())
            print('\nВыпал бочонок', self._barrel)

            self.player.show_card()
            self.cpu.show_card()
            print('\nПоищем эту цифру в карточке компьютера')
            self.mark_num_in_cpu_card()
            self.process_user_choice()

    def check_winner(self):
        pass


    def mark_num_in_cpu_card(self):
        if self.barrel_in_card(self.cpu._card):
            print('\nБочонок с номером {} есть в карточке компьютера, заменим'.format(self._barrel))
            self.replace(self.cpu._card)

    def process_user_choice(self):
        barrel_in_card = self.barrel_in_card(self.player._card)
        player_choice = self._player_choice()

        if player_choice and barrel_in_card:
            print('вызываем replace')
            self.replace(self.player._card)

        elif player_choice and not barrel_in_card:
            print('В твоей карточке нет такого номера!'
                  'Игрок проиграл!')
            self.exit = True

        elif not player_choice and barrel_in_card:
            print('Игрок ошибся и выбрал продолжить. Поражение!')
            self.exit = True

        elif not player_choice and not barrel_in_card:
            print('Игрок выбрал продолжить, берем следующий бочонок\n')

    def check_card_for_win(self, card):
        tmp_counter = 0
        for line in card:
            for j in range(len(line)):
                if line[j] == '-':
                    tmp_counter += 1
                if tmp_counter == 5:
                    return True
            tmp_counter = 0
        return False

    def replace(self, card):
        for line in card:
            for j in range(len(line)):
                if line[j] == self._barrel:
                    line[j] = '-'
                    print('Заменили...\n')

    def barrel_in_card(self, card):
        for sublist in card:
            if self._barrel in sublist:
                return True
        return False


    def _player_choice(self):
        while not self.exit:
            answer = int(input('Что вы хотите сделать?\n'
                           'Нажмите 1 если хотите зачеркнуть. \n'
                           'Нажмите 2 если хотите продолжит. \n'
                            'Нажмите 3 для выхода:'))
            if answer == 3:
                print('До свидания!')
                self.exit = True
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

    game = Game(player, cpu, bag)
    game.start()
