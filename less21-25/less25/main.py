''' 
16:48PM 9/11/2021
#25.Вложенные циклы. Примеры задач с вложенными циклами 
'''

# for i in range(1, 4):
#     for j in range(1, 6):
#         print(f"i = {i}, j = {j}", end=' ')
#     print()

#
#
#

# a = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]

# for row in a:
#     for x in row:
#         print(x, type(x), end = ' ')
#     print()

#
#
#

# a = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
# b = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
# c = []

# for i, row in enumerate(a):
#     r = []
#     for j, x in enumerate(row):
#         r.append(x + b [i][j])
    
#     c.append(r)

# print(c)

#
#
#


# t = [
#     "- Скажи-ка, дядя, ведь не даром",
#      "Я Python выучил с каналом",
#      "Балакирев что   раздавал?",
#      "Ведь  были ж заданья боевые,",
#      "Да, говорят,  ещё какие!",
#      "Недаром помнит вся Россия",
#      "Как мы убили   их тогда!"
#     ]

# for i, line in enumerate(t):
#     while line.count('  '):
#         line = line.replace('  ', ' ')

#     t[i] = line

# print(t)


#
#
#


# M, N = list(map(int, input("Введите M и N: ").split()))

# zeros = []
# for i in range(M):
#     zeros.append([0] * N)

# print(zeros)

# for i in range(M):
#     for j in range(N):
#         zeros[i][j] = 1

# print(zeros)


#
#
#

A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

for r in A:
    for x in r:
        print(x, end=" ")
    print()

print("___________________________________\n")

for i in range(len(A)):
    for j in range(i+1, len(A)):
        A[i][j], A[j][i] = A[j][i], A[i][j]

for r in A:
    for x in r:
        print(x, end=" ")
    print()


