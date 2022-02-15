''' 
17:40PM 9/11/2021
#27.Генераторы списков (List comprehensions)
'''

# [0^2, 1^2, 2^2, 3^2, ..., N^2]
# N - натуральное число

# N = 6
# a = [0] * N

# for i in range(N):
#     a[i] = i ** 2

# print(a)

#
#

# N = 6
# a = [x ** 2 for x in range(N)]
# print(a)

#
#

# d_inp = input("Целые числа через пробел: ")

# a = [int(d) for d in d_inp.split()] 
# d_inp = list(map(int, input("Целые числа через пробел: ").split()))
# print(d_inp)

#
#
#

d = [4, 3, -5, 0, 2, 11, 122, -8, 9]

a = ["четное" if x % 2 == 0 else "нечетное" 
    for x in d
    if x > 0
    ]

print(a)