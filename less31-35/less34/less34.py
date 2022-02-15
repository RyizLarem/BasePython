''' 
23:07PM 9/11/2021
#34.Генераторы множеств и генераторы словарей.
'''
# множество
# a = {x ** 2 for x in range(1, 5)}
# print(a)

# словарь
# a = {x: x ** 2 for x in range(1, 5)}
# print(a)


# d = [1, 2, '1', -4, 3, 4]
# a = {int(x) for x in d}
# set_d = set()
# for x in d:
#     set_d.add(int(x))

# print(set_d)
# print(a)


# m = {"неудовл.": 2, "удовл.": 3, "хорошо": '4', "отлично": '5'}
# a = {key.upper(): int(value) for key, value in m.items()}
# print(a)


# d = [1, 2, '1', '2', -4, 3, 4]
# a = {int(x) for x in d if int(x) > 0}
# print(a)


# replace keys and attribute
m = {"безнадежно": 0, "убого": 1, "неудовл.": 2, "удовл.": 3, "хорошо": '4', "отлично": '5'}

a = {int(value): key for key, value in m.items() if 2 <= int(value) <= 5}
print(a)

