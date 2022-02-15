''' 
19:32PM 9/11/2021
#29.Введение в словари (dict).Базовые операции над словарями.
'''


d = {"house": "дом", "car": "машина",
    "tree": "дерево", "road": "дорога",
    "river": "река"}

print(d)


# проверка состоит ли ключ в словаре
print("house" in d)
print("test" in d)
# этот ключ не входит в словарь - "d"
print("test1" not in d)

''' 
Рассматриваем новую коллекцию языка Python - словарь. Способ задания словарей через фигурные скобки и функцию dict(). Базовые операции со словарями: 
- функция len() для определения числа элементов в словаре;
- оператор del - удаление элемента по ключу;
- оператор in - проверка наличия ключа в словаре.
'''