''' 
22:46PM 9/11/2021
#33.Операции над множествами, сравнение множеств
'''
#
''' 

setA & setB - общие элементы A и B, результат пересечения

res = setA & setB
setA.intersection(setB)
setA.intersection_update(setB)
#
>>> setA.intersection_update(setB)
>>> setA
{3, 4}
#
setA | setB - объединение множеств, возвращает новое множество, старые не меняются
setA.union(setB) == setA | setB


setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6, 7}

setA - setB -> {1, 2} так как 3 и 4 в множестве setB есть, остаётся {1, 2}
setB - setA -> {5, 6, 7} так как 3 и 4 в множестве setA есть, остаётся {5, 6, 7}

#
#
#

>>> setA = {1, 2, 3, 4}
>>> setB = {3, 4, 5, 6, 7}
>>> setA ^ setB
{1, 2, 5, 6, 7}
Показывает элементы которые не совпадают - 3 и 4, были отброшенны

setA != setB
setA == setB

setA < setB
setA > setB

и т.д

'''