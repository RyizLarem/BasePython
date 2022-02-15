''' 
18:31PM 10/11/2021
#39.Функции с произвольным числом параметров *args и **kwargs
'''

# m = max(1, 2, 3, 4, 5)
# print(m)


def os_path(*args, **kwargs):
#    print(kwargs)
    path = kwargs['sep'].join(args)
    return path


p = os_path("F:\\~stepil.org",
            "Добрый, добрый Python (Питон)",
             "39\\p39. Функции.docx",
             sep='|')
print(p)























