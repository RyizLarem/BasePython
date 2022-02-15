''' 
10:00PM 10/11/2021
#37.Алгоритм Евклида для нахождения НОД
'''

import time



# def get_nod(a, b):
#     """Вычисляется НОД для натуральных чискл a и b
#         по алгоритму Евклида.
#     :param a: первое натуральное число
#     :param b: второе натуральное число
#     :return: НОД
#     """

#     while a != b:
#         if a > b:
#             a -= b
#         else:
#             b -= a
        
#     return a


def get_nod(a, b):
    """Вычисляется НОД для натуральных чискл a и b
        по быстрому алгоритму Евклида.
    :param a: первое натуральное число
    :param b: второе натуральное число
    :return: НОД
    """
    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a




def test_nod(func):
    # --- тест №1 ------------
    a = 28
    b = 35
    res = func(a, b)
    if res == 7:
        print("#test1 - ok")
    else:
        print("#test1 - fail")

    # --- тест №2 ------------

    a = 100
    b = 1
    res = func(a, b)
    if res == 1:
        print("#test2 - ok")
    else:
        print("#test2 - fail")

    # --- тест №3 ------------

    a = 2
    b = 1000000000000000000
    st = time.time()
    res = func(a, b)
    et = time.time()
    dt = et - st
    if res == 2 and dt < 1:
        print("#test3 - ok")
    else:
        print("#test3 - fail")


# res = get_nod(18, 24)
# print(res)
# help(get_nod)
test_nod(get_nod)





