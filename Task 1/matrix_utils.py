import os
import random
from typing import Iterable, TypeVar


def generate_random_numeric_matrix(rows_count: int, colums_count: int, min_value: int, max_value: int) -> list[list[int]]:
    return [[random.randint(min_value, max_value) for _ in range(colums_count)] for _ in range(rows_count)]


def matrix_to_string(matrix: list[list[TypeVar('T')]], sep: str = '\t') -> str:
    return os.linesep.join(sep.join(str(cell) for cell in row) for row in matrix)


def iterate_upper_left_triangle(matrix: list[list[TypeVar('T')]], include_additional_diagonal: bool = True) -> Iterable[TypeVar('T')]:
    exclude_count = 1 if include_additional_diagonal else 0
    for row_index in range(len(matrix) - 1, -1, -1):
        for cell_index in range(min(row_index + exclude_count, len(matrix[row_index]))):
            yield matrix[row_index][cell_index]


def iterate_down_right_triangle(matrix: list[list[TypeVar('T')]], include_additional_diagonal: bool = True) -> Iterable[TypeVar('T')]:
    exclude_count = 1 if include_additional_diagonal else 0
    for row_index in range(len(matrix) - 1, -1, -1):
        for cell_index in range(len(matrix) - row_index - exclude_count, len(matrix[row_index])):
            yield matrix[row_index][cell_index]
