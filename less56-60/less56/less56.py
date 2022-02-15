'''
#56.Функция map. Примеры её использования.
'''


# def symbols(s):
#     return list(s.lower())


cities = ["Москва", "Астрахань", "Самара", "Уфа", "Смоленск", "Тверь"]

b = map(lambda s: s[::-1], cities)

a = list(b)
print(a)

# b = map(int, ['1', '2', '3', '5', '7'])
# b = (int(x) for x in ['1', '2', '3', '5', '7'])


# for x in b:
#     print(x, end=" ")
    

# a = min(b)
# print(a)


# s = map(int, input().split())
# a = list(s)
# print(a)
# >>> 1 2 3 4
# >>> [1, 2, 3, 4]
