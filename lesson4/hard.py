# Задание:
# Эта программа являет собой упрощенный симулятор банкомата, пользователь вводит номер карты и пин код,
# в случае успеха программа предлагает меню для выбора действий, где он может проверить счет, или снять деньги.
#
# Эта задача не так похожа на другие, но она, как никогда прежде приближена к реалиям разработки общего проекта.
#
# Ваша задача исправить ошибки логики, и выполнить проверки данных, которые вводит пользователь.
# Обязательно убедитесь, что вы выполнили все проверки, попробуйте сами сломать свою программу вводя неверные данные!

person1 = {'card': 4276123465440000, 'pin': 9090, 'money': 100.90}
person2 = {'card': 4276123465440001, 'pin': 9091, 'money': 200.90}
person3 = {'card': 4276123465440002, 'pin': 9092, 'money': 300.90}
# person1 =  4276123465440000 9090
# person2 = 4276123465440001 9091
# person3 = 4276123465440002 9092
# bad input 4276123465440002 9091
bank = [person1, person2, person3]

# def check_card_number_and_pin(card_number, pin_code):
#     card_number = str(card_number)
#     pin_code = str(pin_code)
#     card_ok = re.search(card_pattern, card_number)
#     pin_ok = re.search(pin_pattern, pin_code)
#     if card_ok and not pin_ok:
#         print('Пин введен не верно')
#     elif not card_ok and pin_ok:
#         print('Номер карты введен не верно')
#     elif not card_ok and not pin_ok:
#         print('Номер карты и пин введены не верно')


def get_person_by_card(card_number):
    for person in bank:
        if person['card'] == card_number:
            return person


def is_pin_valid(person, pin_code):
    if person['pin'] == pin_code:
        return True
    return False


def check_account(person):
    return round(person['money'], 2)


def withdraw_money(person, count):
    if person['money'] - count >= 0:
        person['money'] -= count
        return 'Вы сняли {} рублей.'.format(count)
    else:
        return 'На вашем счету недостаточно средств!'


def process_user_choice(choice, person):
    # print('user choice is >>', choice)
    if choice == 1:
        print(check_account(person))
    elif choice == 2:
        count = float(input('Сумма к снятию:'))
        print(withdraw_money(person, count))


def start():
    try:
        card_number, pin_code = input('Введите номер карты и пин код через пробел:').split()
    except ValueError:
        print('Вы допустили ошибку во время ввода, введите номер карты и пин код через пробел')
    except Exception:
        print('Неизвестная ошибка, введите номер карты и пин код через пробел')
    # print(card_number, pin_code)
    card_number = int(card_number)
    pin_code = int(pin_code)
    person = get_person_by_card(card_number)
    if person and is_pin_valid(person, pin_code):
        while True:
            choice = int(input('Выберите пункт:\n'
                               '1. Проверить баланс\n'
                               '2. Снять деньги\n'
                               '3. Выход\n'
                               '---------------------\n'
                               'Ваш выбор:'))
            if choice == 3:
                break
            else:
                # print('choice is: ', choice)
                process_user_choice(choice, person)
    else:
        print('Номер карты или пин код введены не верно!')
        # check_card_number_and_pin(card_number, pin_code)





start()