''' 
16:19PM 8/11/2021
#21.Операторы циклов break, continue и else
'''

# d = [1, 5, 3, 6, 0, -4]

# flFind = False

# print("запуск цикла")

# i = 0
# while i < len(d):
#     print(i)
#     flFind = d[i] % 2 == 0
#     if flFind:
#         break

#     i += 1

# print(flFind)
# print("завершение цикла")

#
#
#


# s = 0
# d = 1

# while d != 0:
#     d = int(input("Введите целое число: "))
#     if d % 2 == 0:
#         continue

#     s += d
#     print("s = " + str(s)) 


#
#
#

# S = 1/2 + 1/3 + 1/4 + 1/10 + ... + 1/0


S = 0 
i = -10

while i < 100:
    if i == 0:
        break
    S += 1/i
    i += 1
else: 
    print("Сумма вычислена ккорректно")

print(S)


