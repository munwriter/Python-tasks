"""Определть есть ли в двумерном списке столбец с одинаковым количеством положительных и отрицательных чисел."""


import random


def matrix_generator(col: int, row: int) -> list[list[int]]:
    return [[random.randint(-10, 10) for j in range(col)] for i in range(row)]


def matrix_transposition(matrix: list[list[int]]) -> list[list[int]]:
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


def matrix_positive_and_negative_counter(matrix: list[int]) -> list[int]:
    positive = len(list(filter(lambda x: x > 0, matrix)))
    negative = len(list(filter(lambda x: x < 0, matrix)))
    return [positive, negative]


def is_positive_and_negative_numbers_same(matrix: list[list[int]]) -> bool:
    matrix = matrix_transposition(matrix)
    for i in range(len(matrix)):
        pos_neg = matrix_positive_and_negative_counter(matrix[i])
        if pos_neg[0] == pos_neg[1]:
            return True
    return False


matrix = matrix_generator(4, 2)
print(is_positive_and_negative_numbers_same(matrix), matrix)
