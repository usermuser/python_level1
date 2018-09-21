# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

class TownCar():
    def __init__(self, speed, color, name, is_police=False):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        print('Машина {} поехала.'.format(self.name))

    def stop(self):
        print('Машина {} остановилась.'.format(self.name))

    def turn(self, direction):
        print('Машина {} повернула {}.'.format(self.name, direction))


class SportCar():
    def __init__(self, speed, color, name, is_police=False):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина {} поехала.'.format(self.name))

    def stop(self):
        print('Машина {} остановилась.'.format(self.name))

    def turn(self, direction):
        print('Машина {} повернула {}.'.format(self.name, direction))


class WorkCar():
    def __init__(self, speed, color, name, is_police=False):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина {} поехала.'.format(self.name))

    def stop(self):
        print('Машина {} остановилась.'.format(self.name))

    def turn(self, direction):
        print('Машина {} повернула {}.'.format(self.name, direction))


class PoliceCar():
    def __init__(self, speed, color, name, is_police=True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина {} поехала.'.format(self.name))

    def stop(self):
        print('Машина {} остановилась.'.format(self.name))

    def turn(self, direction='None'):
        if direction == 'None':
            print('Направление не указано')
            return
        print('Машина {} повернула {}.'.format(self.name, direction))


lexus = TownCar(100, 'красный', 'лексус', 1)
lexus.go()
lexus.turn('налево')
print(lexus.color)
print(lexus.is_police)

ferrari = SportCar(200, 'белый', 'феррари')
print(ferrari.color)
ferrari.go()

kamaz = WorkCar(80, 'оранжевый', 'камаз')
kamaz.go()
kamaz.turn('лево')
kamaz.stop()

uaz = PoliceCar('120', 'Сине-белый', 'УАЗ')
print(uaz.name)
uaz.go()
print(uaz.is_police)
uaz.turn()

print(uaz.speed)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.
print('\nЗадача-2.\n')
class Car():
    def __init__(self, speed, color, name, is_police=False):
        print('init отработал')
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина {} поехала.'.format(self.name))

    def stop(self):
        print('Машина {} остановилась.'.format(self.name))

    def turn(self, direction='None'):
        if direction == 'None':
            print('Направление не указано')
            return
        print('Машина {} повернула {}.'.format(self.name, direction))

lexus = Car(100, 'синий', 'lexus')
lexus.go()
lexus.turn('направо')

kamaz = Car(80, 'черный', 'камаз')
kamaz.go()
kamaz.turn('налево')
kamaz.stop()