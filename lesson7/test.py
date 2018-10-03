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


# lst1 = ['1', '52', ' ', '88', ' ']
# lst2 = ['22', ' ', '33', ' ', '66']
# lst3 = [' ', ' ', '45', '75', '85']
# lst4 = [lst1, lst2, lst3]
# print('lst4 = ', lst4)
#
# for i in lst4:
#     if '1' in i:
#         print('yes')


# # print(' '.join(lst3))
#
# for i in lst4:
#     r = '45'
#     for j in i:
#         if r in j:
#             r.replace(r, '-')
#             r.re
#
# print(lst4)

# a = [1,2,3,2,3,4,3,5,6,6,5,4,5,4,3,4,3,2,1]
# map(lambda x:x if x!= 4 else 'sss',a)
# [1, 2, 3, 2, 3, 'sss', 3, 5, 6, 6, 5, 'sss', 5, 'sss', 3, 'sss', 3, 2, 1]

# lst4 = list(map(lambda x:x if x!='45' else '-', lst4))
# print(lst4)

# for i in lst4:
#     for j in i:
#         # print(j)
#         if j == '45':
#             e = j.index('45')
#             print(e)
#             i[e] = '-'
# print(lst4)



def f(lst4):
    for i in lst4:
        for j in range(len(i)):
            if i[j] == '45':
                i[j] = '-'
    return lst4

# print(f(lst4))

# # pass this
# lst5 = []
# for i in lst4:
#     for j in i:
#         lst5.append(j)
# print(' '.join(lst5))
# ########################
#
# def prettify_card(some_list):
#     print('=======start========')
#     for i in some_list:
#         print(' '.join(i))
#     print('=======end==========')
#     return some_list
#
# print('++')
# prettify_card(lst4)
# print('++')
#
# def sum_lists(lst):
#     print('another way to concatenate lists')
#     result = sum([lst[0]+lst[1]+lst[2]], [])
#     # print('my_sum = ', ' '.join(result))
#     return result
#
# one_list= sum_lists(lst4)
# print('one_list = ', one_list)


# c = [1]
# print(True == len(c))

# print(lst5)
# c = 0
# for i in lst5:
#     c +=1
#     print(i)
#     if c == 9:
#         print('z\n')
#         c = 0
# lst = [x for x in range(1,91)]
#
# def generator(lst):
#     while len(lst):
#         a = lst.pop(random.randrange(len(lst)))
#         yield a
#
# a = generator(lst)

# print(next(a))
# print(next(generator(lst)))


# def three_lists(lst):
#     result = []
#     for i in range(3):
#         a = lst[0:10]
#         result.append(a)
#
# print('\n')
# print(three_lists(lst4))

