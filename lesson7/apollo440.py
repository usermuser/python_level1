import random

class ThreeRowsCard():
    def __init__(self, nums_in_row=5):
        self._ROWS_QTY = 3          # rows quantity
        self._NUMS_IN_ROW = nums_in_row
        self._NUMS_RANGE = 90
        self._NUMS_IN_CARD = 15


class Card(ThreeRowsCard):
    def __init__(self):
        super().__init__()
        # список случайных номеров для карточки
        self.nums_for_card = random.sample(range(1, self._NUMS_RANGE+1), self._NUMS_RANGE)

    def _create_line(self):
        output_list = []
        for _ in range(self._NUMS_IN_ROW):
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
        for _ in range(self._ROWS_QTY):
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
        self.BARRELS_IN_BAG = 91
        self._barrels = [x for x in range(1, self.BARRELS_IN_BAG)]

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
        self._NUMS_TO_WIN = 15


    def start(self):

        while not self.exit:
            self._barrel = str(bag.get_barrel())
            print('\nВыпал бочонок', self._barrel)

            self.player.show_card()
            self.cpu.show_card()
            print('\nПоищем эту цифру в карточке компьютера')
            self.mark_num_in_cpu_card()
            self.process_user_choice()
            if self.check_winner():
                break

    def check_winner(self):
        if self.check_card_for_win(self.player._card):
            print('Игрок победил')
            return True
        elif self.check_card_for_win(self.cpu._card):
            print('Компьютер победил')
            return True
        else:
            return False



    def mark_num_in_cpu_card(self):
        if self.barrel_in_card(self.cpu._card):
            print('\nБочонок с номером {} есть в карточке компьютера, заменим'.format(self._barrel))
            self.replace(self.cpu._card)

    def process_user_choice(self):
        is_barrel_in_card = self.barrel_in_card(self.player._card)
        player_choice = self._player_choice()

        if player_choice and is_barrel_in_card:
            print('вызываем replace')
            self.replace(self.player._card)

        elif player_choice and not is_barrel_in_card:
            print('В твоей карточке нет такого номера!'
                  'Игрок проиграл!')
            self.exit = True

        elif not player_choice and is_barrel_in_card:
            print('Игрок ошибся и выбрал продолжить. Поражение!')
            self.exit = True

        elif not player_choice and not is_barrel_in_card:
            print('Игрок выбрал продолжить, берем следующий бочонок\n')

    def check_card_for_win(self, card):
        tmp_counter = 0
        for line in card:
            for j in range(len(line)):
                if line[j] == '-':
                    tmp_counter += 1
                if tmp_counter == self._NUMS_TO_WIN:
                    return True
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
