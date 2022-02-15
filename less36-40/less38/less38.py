''' 
11:40PM 10/11/2021
#38.Именованные аргументы. Фактические и формальные параметры
'''


# def get_V(a, b, c, verbose=True):
#     if verbose:
#         print(f"a = {a}, b = {b}, c = {c}")

#     return a * b * c


# v = get_V(1, 2, 3)http://word-office.ru/kak-sdelat-obtekanie-tekstom-v-powerpoint-2007.html
# print(v)

#
#

# def cmp_str(s1, s2, reg=False, trim=True):
#     if reg:
#         s1 = s1.lower()
#         s2 = s1.lower()
#     if trim:
#         s1 = s1.strip()
#         s2 = s1.strip()

#     return s1 == s2


# print(cmp_str("Python", " PYTHON"))

#
#

# def add_value(value, lst=[]):

#     lst.append(value)

#     return lst


# l = add_value(1)
# l = add_value(2)
# print(l)
# список не пустой вызывается, он же изменяемый тип данных

#
#

def add_value(value, lst=None):
    if lst is None:
        lst = []

    lst.append(value)

    return lst


l = add_value(1)
l = add_value(2, l)
print(l)
