''' 
19:12PM 9/11/2021
#28.Вложенные генераторы списков
'''


# a = [(i,j) 
#     for i in range(3) if i % 3 == 0
#         for j in range(4) if j % 2 == 0
#     ]

# print(a)

#
#

# Таблица умножения
# a = [f"{i}*{j} = {i*j}"
#     for i in range(10)
#     for j in range(10)
#     ]

# print(a)

#
#

# matrix = [[0, 1, 2, 3],
#           [10, 11, 12, 13],
#           [20, 21, 22, 23]]

# a = [x
#     for row in matrix
#     for x in row
#     ]

# print(a)


#
#


# M, N = 3, 4
# matrix = [[a for a in range(M)] for b in range(N)]
stop
# print(matrix)


#
#A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

# A = [[row[i] for row in A] for i in range(len(A[0]))]



# print(A)


# A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# AA = [[x ** 2 for x in row] for row in A]
# a = [x **2
#     for row in A
#     for x in row
#     ]


# print(AA)
# print(a)


#
#


# A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

# A = [[row[i] for row in A] for i in range(len(A[0]))]

# print(A)


#
#


# [for<varibles> in [generator list]]

# g = [u ** 2 for u in [x+1 for x in range(5)]]

# g(u(x+1)) = (x+1)^2


g = [u ** 2 for u in [x + 1 for x in range(5)]]

print(g)
