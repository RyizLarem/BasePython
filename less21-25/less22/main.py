''' 
16:42PM 8/11/2021
#22.Оператор цикла for. Функция range() 
'''

# d = [1, 2, 3, 4, 5, 3, 4,55,6,6,6,6,6]

# p = 1
# for i in range(len(d)):
#     d[i] = 0

# print(d)

#
#
#

# S = 1/2 + 1/3 + 1/4 + ... + 1/1000

S = 0
for i in range(2, 1001):
    S += 1/i

print(S)