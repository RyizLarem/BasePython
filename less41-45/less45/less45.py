''' 
10:09AM 11/11/2021
#45.Введение в декораторы функций
'''

import time


# def func_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("------------ что-то делает перед вызовом функции ------------")
#         res = func(*args, **kwargs)
#         print("------------ что-то делает после вызова функции ------------")
#         return res

#     return wrapper


# def some_func(title, tag):
#     print(f"title = {title}, tag = {tag} ")
#     return f"<{tag}>{title}</{tag}>"


# some_func = func_decorator(some_func)
# res = some_func("Python навсегда!", "h1")
# print(res)


#
#
#


def test_time(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        res = func(*args, **kwargs)
        et = time.time()
        dt = et - st
        print(f"Время работы: {dt} сек")
        return res

    return wrapper

@test_time
def get_nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


@test_time
def get_fast_nod(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b

    return a



# get_nod = test_time(get_nod)
# get_fast_nod = test_time(get_fast_nod)

# res = get_nod(2, 10000)
# res2 = get_fast_nod(2, 100)
# print(res, res2)


get_fast_nod(2, 10000)






