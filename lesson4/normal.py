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
# user_input = 'Василий Пупкин'
name, surname = user_input.split()
# print('name:', name, 'surname:', surname)

# name_pattern = '^[А-Я][а-я]+$|^[A-Z][a-z]+$'
pattern = '^[А-Я][а-я]+$|^[A-Z][a-z]+$'

def check_user_input(pattern, input):
    search_result = re.search(pattern, input)
    # print(search_result)
    if search_result:
        return True
    else:
        return False


name_ok = check_user_input(pattern, name)
surname_ok = check_user_input(pattern, surname)

if name_ok and surname_ok:
    print(name, surname, ' - Данные введены верно')
elif not name_ok and surname_ok:
    print(name, surname, ' - Неверно указано имя')
elif name_ok and not surname_ok:
    print(name, surname, ' - Неверно указана фамилия')
elif not name_ok and not surname_ok:
    print(name, surname, ' - Неверно указаны имя и фамилия')


print('\nПроверка email')
# email = input('Введите email.')
mail = 'te_4_st@test.com'
email = 'te$T@test.net'
old_email_pattern = '^[(a-z0-9\_)]+\@[a-z0-9]+\.(ru|com|org)$'
email_pattern = '^([a-z0-9\_]+)\@[a-z0-9]+\.(ru|com|org|рф)$'


email_result = re.search(email_pattern, email)
print(email_result)
if email_result:
    print(email_result.group(1))
    print(email_result.group(2))
else:
    if

# email_result = check_user_input(email_pattern, bad_email)
# print(email_result)

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