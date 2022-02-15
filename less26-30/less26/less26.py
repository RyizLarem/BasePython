''' 
17:24PM 9/11/2021
#26.Треугольниик Паскаля как пример работы вложенных циклов
'''

N = 18
P = []

for i in range(N):
    row = [1] * (i+1)
    for j in range(i * 1):
        if j != 0 and j != 1:
            row[j] = P[i-1][j-1] + P[i-1][j]

    P.append(row)

for r in P:
    print(r)