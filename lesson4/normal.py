# Эти задачи необходимо решить используя регулярные выражения!

# Задача - 1
# Запросите у пользователя имя, фамилию, email. Теперь необходимо совершить проверки,
# имя и фамилия должны иметь заглавные первые буквы.
# email - не должен иметь заглавных букв и должен быть в формате: текст в нижнем регистре,
#  допускается нижнее подчеркивание и цифры, потом @, потом текст, допускаются цифры,
#  точка, ru или org или com.
# Например:
# Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email
#  (спецсимвол, заглавная буква, .net), te_4_st@test.com - верно указан.
import re

# Так как язык не указан, значит разрешено вводить Василий Пупкин или Vasiliy Pupkin
user_input = input('Введите имя и фамилию с заглавной буквы:')
name, surname = user_input.split()

pattern = '^[А-Я][а-я]+$|^[A-Z][a-z]+$'

name_ok = re.search(pattern, name)
surname_ok = re.search(pattern, surname)

if name_ok and surname_ok:
    print(name, surname, ' - Данные введены верно')
elif not name_ok and surname_ok:
    print(name, surname, ' - Неверно указано имя')
elif name_ok and not surname_ok:
    print(name, surname, ' - Неверно указана фамилия')
elif not name_ok and not surname_ok:
    print(name, surname, ' - Неверно указаны имя и фамилия')

print('\nПроверка email.')
email = input('Введите email: ')
# email = 'te_4_st@test.com'
# email = 'te$T@test.net'

# создадим словарь, который хранит все регулярные выражения
patterns = {'email_pattern': '^([a-z0-9\_]+)\@[a-z0-9]+\.(ru|com|org|рф)$',
            'caps_pattern': '[A-ZА-Я]',
            'dotnet_pattern': '(.net)$',
            'special_symbol_pattern': '[\,\?\!\#\$\%\^\&\*]'}

# создадим функцию, которая проверит где именно ошибка
# данная функция позволяет добавить проверки при необходимости
# не изменяя базовую логику программы
def check_bad_email(**kwargs):
    result = ''

    dotnet_pattern = kwargs['dotnet_pattern']
    caps_pattern = kwargs['caps_pattern']
    special_symbol_pattern = kwargs['special_symbol_pattern']

    dotnet = re.search(dotnet_pattern, email)
    caps = re.search(caps_pattern, email)
    special_symbol = re.search(special_symbol_pattern, email)

    if special_symbol:
        result += '- спецсимволы недопустимы\n'
    if dotnet:
        result += '- .net не допустимо\n'
    if caps:
        result += '- заглавные буквы недопустимы\n'
    print('Введен недопустимый email: ', email)
    print(result)

# сначала проверим, что введенный email правильный
basic_email_check_ok = re.search(patterns['email_pattern'], email)

if basic_email_check_ok:
    print(email, ' - указан верно')
else:
    check_bad_email(**patterns)

# Задача - 2:
# Вам дан текст:

some_str = '''
Мороз и солнце; день чудесный!
Еще ты дремлешь, друг прелестный —
Пора, красавица, проснись:
Открой сомкнуты негой взоры
Навстречу северной Авроры,
Звездою севера явись!
Вечор, ты помнишь, вьюга злилась,
На мутном небе мгла носилась;
Луна, как бледное пятно,
Сквозь тучи мрачные желтела,
И ты печальная сидела —
А нынче... погляди в окно:
Под голубыми небесами
Великолепными коврами,
Блестя на солнце, снег лежит;
Прозрачный лес один чернеет,
И ель сквозь иней зеленеет,
И речка подо льдом блестит.
Вся комната янтарным блеском
Озарена. Веселым треском
Трещит затопленная печь.
Приятно думать у лежанки.
Но знаешь: не велеть ли в санки
Кобылку бурую запречь?
Скользя по утреннему снегу,
Друг милый, предадимся бегу
Нетерпеливого коня
И навестим поля пустые,
Леса, недавно столь густые,
И берег, милый для меня.'''

# Необходимо с помощью регулярных выражений определить есть ли в тексте подряд
# более одной точки, при любом исходе сообщите результат пользователю!
