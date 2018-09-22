import random

# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.
print('Задача-1.\n')


class Toy():
    def __init__(self, name, color, type):
        self.name = name
        self.color = color
        self.type = type

    def _buy_blank(self):
        print('Закупаем сырье')

    def _paint(self):
        print('Красим игрушку в {} цвет'.format(self.color))

    def _sew(self):
        print('Пошив игрушки {}'.format(self.name))


class Factory(Toy):
    def __init__(self, name, color, type):
        super().__init__(name, color, type)
        self.create_toy()

    def create_toy(self):
        self._buy_blank()
        self._paint()
        self._sew()
        print('Создалась игрушка с параметрами: цвет: {}, имя {}, тип: {}'.format(self.color, self.name, self.type))


batman = Factory('бэтмэн', 'черный', 'персонаж мультфильма')

print('\n==============================================================================================')

print('\nЗадача-2.\n')


# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка
class Base_Toy():
    def __init__(self, type, name='empty', color='empty'):
        self.name = name
        self.color = color
        self.type = type

    def _buy_blank(self):
        print('\nЗакупаем сырье')

    def _paint(self):
        print('Красим игрушку в {} цвет'.format(self.color))

    def _sew(self):
        print('Пошив игрушки {}'.format(self.name))


class Cartoon_Character(Base_Toy):
    def __init__(self, type):
        super().__init__(type)
        self.character_choice = random.choice(['бэтмэн', 'человек-паук'])  # случайным образом решаем бэтмен или паучок
        self.type = 'персонаж мультфильма'

        if self.character_choice == 'человек-паук':
            self.name = self.character_choice
            self.color = 'синий'
        else:
            self.name = self.character_choice
            self.color = 'черный'

    def create_cartoon_character(self):
        self._buy_blank()
        self._paint()
        self._sew()
        print('Создалась игрушка с параметрами: цвет: {}, имя {}, тип: {}'.format(self.color, self.name, self.type))


class Animal(Base_Toy):

    def create_animal(self):
        animal_choice = random.choice(['кот', 'собака'])  # рандомно выбираем животное
        self.name = animal_choice

        if animal_choice == 'собака':  # у собак свой цвет
            self.color = 'белый цвет с черными пятнами'
            self._create_dog()
        else:
            self.color = 'белый'  # у кошек свой
            self._create_cat()

    def _paint_cat(self):
        print('Красим нашу кошку в белый цвет')

    def _paint_dog(self):
        print('Красим нашу собаку в {}'.format(self.color))

    def _create_cat(self):
        self._buy_blank()
        self._paint_cat()
        self._sew()
        print('Создалась игрушка с параметрами: цвет: {}, имя {}, тип: {}'.format(self.color, self.name, self.type))

    def _create_dog(self):
        self._buy_blank()
        self._paint_dog()
        self._sew()
        print('Создалась игрушка с параметрами: цвет: {}, имя {}, тип: {}'.format(self.color, self.name, self.type))


class Factory2(Cartoon_Character, Animal):
    def __init__(self, type):
        super().__init__(type)
        self.type = type
        self.create()  # в конструкторе вызываем функцию создающую игрушку

    def create(self):
        if self.type == 'персонаж мультфильма':
            self.create_cartoon_character()
        elif self.type == 'животное':
            self.create_animal()
        else:
            print('\nНе верно указан тип игрушки:', self.type,
                  '\nНаша фабрика шьет либо "животное", либо "персонаж мультфильма"')


cartoon_character = Factory2('персонаж мультфильма')
animal = Factory2('животное')
animal42 = Factory2('живот')
