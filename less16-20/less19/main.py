''' 
PM 8/11/2021
#19.Тернарный оператор. Вложенное тернарное условие
'''

# a = -12
# b = -7

# # if a > b:
# #     res = a
# # else:
# #     res = b

# res = a if a > b else b
# print(res)

#
#
#

s = "python"
t = 'upper'

res = s.upper() if t == 'upper' else s
print(res)


''' 
>>> a = 12
>>> "a - " + ("четное" if a % 2 == 0 else "нечетное") + " число"
'a - четное число'
>>> 

#
#
#

>>> max(1, 5, a if a > 0 else b, 4, 5)
12
>>> a = 167
>>> max(1, 5, a if a > 0 else b, 4, 5)
167
>>> 
'''

a = 2
b = 3
c = 5

d = (a if a > c else c) if a > b else (b if b > c else c)
print(d)