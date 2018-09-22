# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

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


# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка

class Toy2():
    def __init__(self, name, color, type):
        self.name = name
        self.color = color
        self.type = type

    def _buy_blank(self):
        print('Закупаем сырье')

    def _paint(self):
        print('Красим игрушку в {} цвет'.format(self.color))

    def _sew(self):
        print('Пошив {}'.format(self.name))


class Cartoon_Character(Toy2):

    def create_spider_man(self):
        self._buy_blank()
        self._paint()
        self._sew()
        print('Создалась игрушка с параметрами: цвет: {}, имя {}, тип: {}'.format(self.color, self.name, self.type))

    def create_batman(self):
        self._buy_blank()
        self._paint()
        self._sew()
        print('Создалась игрушка с параметрами: цвет: {}, имя {}, тип: {}'.format(self.color, self.name, self.type))

class Animal(Toy2):
    def create_cat(self):
        pass

    def create_dog(self):
        pass


class Factory(Cartoon_Character, Animal):


