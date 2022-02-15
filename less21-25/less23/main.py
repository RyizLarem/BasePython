''' 
15:41PM 9/11/2021
#23.Примеры работы оператора цикла for. Функция enumerate()
'''
# n! = 1*2*3*...*n - Вычисление факториала от натурального числа n:


# n = int(input("Введите натуральное число не более 100: "))

# if n < 1 or n > 100:
#     print("Неверне введено натуральное число")
# else:
#     p = 1
#     for i in range(1, n+1):
#         p *= i
    
#     print(f"Факториал {n}! = {p}")


# звёздочки
# for i in range(1, 11):
#     print('*' * i)

#

words = ["Python", "дай", "мне", "силы", "пройти", "этот", "курс", "до", "конца"]

# s = ''
# fl_first = True
# for w in words:
#     s += ('' if fl_first else ' ') + w
#     fl_first = False 

# print(s)
# Лучше использвовать lstrip() - для удаления пробелов

# альтернатива
# print(" ".join(words))

#
#
#

# замена всех двух значных элементов списка на нули
# digs = [4, 3, 100, -53, -30, 1, 34, -8]

# for i in range(len(digs)):
#     if 10 <= abs(digs[i]) <= 99:
#         digs[i] = 0

# print(digs)

# альтернатива

digs = [4, 3, 100, -53, -30, 1, 34, -8]

for i, d in enumerate(digs):
    if 10 <= abs(d) <= 99:
        digs[i] = 0

print(digs)


#
#
#


# Преобразование кириллици в латиницу. 

t = ['a', 'b', 'v', 'g', 'd', 'e', 'zh',
     'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p',
     'r', 's', 't', 'u', 'f', 'h', 'c', 'ch', 'sh',
     'shcn', '', 'y', '', 'e', 'yu', 'ya'
    ]

start_index = ord('а')
title = "Программирование на Python - лучший курс"
slug = ''

for s in title.lower():
    if 'а' <= s <= 'я':
        slug += t[ord(s) - start_index]
    elif s == 'ё':
        slug += 'yo'
    elif s in " !?;:.,":
        slug += '-'
    else:
        slug += s

while slug.count('--'):
    slug = slug.replace('--', '-')
    
print(slug)