'''
#58.Функция zip. Примеры использования.
'''


a = [1, 2, 3, 4]
b = [5, 6 ,7 ,8, 9, 10]
c = "python"
d = {'a', 1, 34, "py"}

z = zip(a, b, c, d)
t1, t2, t3, t4 = zip(*z)
print(t1, t2, t3, t4, sep="\n")
# for x in z:
#     print(x)




