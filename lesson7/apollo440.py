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
            output_list.append(num)
            output_list.sort()
            self.nums_for_card.remove(num)

        # вставим пробелы в рандомные позиции
        for _ in range(4): # 4 пробела
            output_list.insert(random.randrange(len(output_list)), ' ')
        return output_list


    def create_card(self):
        output = []
        for _ in range(self._rows_qty):
            output.append(self._create_line())
        # print(*output, sep='\n')
        # for i in output:
        #     print(' '.join(str(i)[1:-1]))
        return output


# t = Card()
# player_card = t.create_card()

class Person():
    pass

class Player(Person):
    def __init__(self):
        self.card = Card().create_card()
        self.card2 = copy.deepcopy(self.card)
        print('Player instance')
        print(self.card2)

    def show_card(self):
        print('= = = = = = YOUR CARD = = = = = = = = = = =')
        for i in self.card2:
            print(' '.join(str(i)))
            # print(i)
        print('= = = = = = = = = = = = = = = = = = = = = =')



class Cpu(Person):
    def __init__(self):
        self.card = Card()

    def take_card(self):
        self.card = Card()


class Game():
    pass

print('startt')
player = Player()
# print(player.show_card())
# cpu = Cpu()

