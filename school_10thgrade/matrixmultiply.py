import random
import numpy as np


def matrix_multiply(matrix1: list[list[int]], matrix2: list[list[int]]) -> list[list[int]]:
    res = [[0 for j in range(col1)] for i in range(row)]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                res[i][j] += matrix1[i][k] * matrix2[k][j]
    return res


def matrix_validator(matrix1: list[list[int]], matrix2: list[list[int]]) -> list[list[int]]:
    if row and row1 and col and col1:
        if len(matrix1[0]) == len(matrix2):
            return (matrix1, matrix2)
        else:
            raise Exception(
                'Кол-во столбцов первой должно быть равно кол-ву строк второй')
    else:
        raise Exception('Размерность матриц должна быть больше 0')


def matrix_generator(col: int, row: int) -> list[list[int]]:
    return [[random.randint(1, 11) for j in range(col)] for i in range(row)]


row = int(input())
col = int(input())
row1 = int(input())
col1 = int(input())

m1 = matrix_generator(col, row)
m2 = matrix_generator(col1, row1)

for i in matrix_multiply(*matrix_validator(m1, m2)):
    print(i)

# print(np.dot(m1, m2))
