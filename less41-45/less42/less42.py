''' 
5:59AM 11/11/2021
#42.Анонимные (lambda) функции.
'''


'''

>>> lambda a, b: a + b
<function <lambda> at 0x7fc3bdc1b1f0>
>>> s = lambda a, b: a + b
>>> s(4, 4)
8

'''


lst = [5, 3, 0, -6, 8, 10, 1]


def get_filter(a, filter=None):
    if filter is None:
        return a
    
    res = []
    for x in a:
        if filter(x):
            res.append(x)

    return res


r = get_filter(lst, lambda x: x % 0 == 0)
print(r)