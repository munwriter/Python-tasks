import random


col = int(input())
row = int(input())

matrix = [[random.randint(1, 11) for j in range(col)] for i in range(row)]
transpose_matrix = []


for i in range(col):
    el = []
    for j in range(row):
        el.append(matrix[j][i])
    transpose_matrix.append(el)

print(matrix)
print(transpose_matrix)

