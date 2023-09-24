"""Создать матрицу произвольного размера, состоящую и найти элемет наиболее близкий к среднему ареф. всех элементов"""


import random


def matrix_generator(col: int, row: int) -> list[list[int]]:
    return [[random.randint(-10, 10) for j in range(col)] for i in range(row)]


def average_element_search(matrix: list[list[int]]) -> float:
    return sum(map(sum, matrix)) / len(matrix[0])


def the_closest_to_average_element_search(matrix: list[list[int]]) -> int:
    average_element = average_element_search(matrix)
    the_closest = matrix[0][0]
    min_shift = abs(matrix[0][0] - average_element)

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if abs(matrix[row][col] - average_element) < min_shift:
                min_shift = abs(matrix[row][col] - average_element)
                the_closest = matrix[row][col]
    return the_closest


mat = matrix_generator(5, 3)
print(mat, the_closest_to_average_element_search(
    mat), average_element_search(mat))
