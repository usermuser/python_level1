import random

# lst = [['a','b','c'], ['x','y','x']]
# a='a'
# b = ['a','b','c']
# print(a in lst)
# print(b in lst)
# # lst.index('b')
#
# print('waza')
# if lst.count(b) > 0:
#     print('yes')

# random.sample(population, k) - список длиной k из последовательности population.
# a = random.sample(range(1, 90), 15)
# print('a = ', a)
# получу пять элеменотв из списка a и положу в b


# def take_5():
#     b = []
#     for _ in range(5):
#         item = random.choice(a)
#         b.append(item)
#         a.remove(item)
#     return b
# print(take_5())

# print('a = ', a)
# print('b = ', b)

# b = random.sample(a, 5)
# # a1 = a - b
# b.sort()
#

# print('b = ', b)
# print('a1 = ', a1)

# вставим 4 пробела в строчке
# for i in range(4):
#     b.insert(random.randrange(len(b)+1), ' ')
# print('b = ', b)

# e = random.randrange(2) # или 0, или 1
# print('e = ', e)


# a = sorted(a)

# print(a)

# print('=== ===')
# for i in range(3):
#     print(i)


# def my_print(func):
#     def wrapper_my_print(*args, **kwargs):
#         print('------ {} -----'.format('Ваша карточка'))
#         value = func(*args, **kwargs)
#         print('--------------------------')
#         return value
#     return wrapper_my_print
#
# @my_print
# def create_card(self):
#     output = []
#
#     for _ in range(self._rows_qty):
#         output.append(self._create_line())
#     print(output)
#
#     return output


lst1 = ['1', '52', ' ', '88', ' ']
lst2 = ['22', ' ', '33', ' ', '66']
lst3 = [' ', '45', '75', ' ', '85']
lst4 = [lst1, lst2, lst3]
print(lst4)
# print(' '.join(lst3))

lst5 = []
c = 0
for i in lst4:
    for j in i:
        lst5.append(j)

print(' '.join(lst5))

print('=======start========')
for i in lst4:
    print(' '.join(i))
print('=======end==========')

# print(lst5)
# c = 0
# for i in lst5:
#     c +=1
#     print(i)
#     if c == 9:
#         print('z\n')
#         c = 0
