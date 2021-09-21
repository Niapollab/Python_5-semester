import sys
from matrix_utils import *
from console_utils import *


def read_random_numeric_matrix_from_console() -> list[list[int]]:
    rows_count = safe_int_input("Введите число строк: ", "Число должно быть строго положительным.", 1)
    colums_count = safe_int_input("Введите число столбцов: ", "Число должно быть строго положительным.", 1)
    min_value = safe_int_input(
        "Введите минимальное значение элемента матрицы: ")
    max_value = safe_int_input(
        "Введите максимальное значение элемента матрицы: ")

    matrix = generate_random_numeric_matrix(
        rows_count, colums_count, min_value, max_value)

    print("Сгенерированная матрица: ")
    print(matrix_to_string(matrix))
    print()

    return matrix


def read_numeric_matrix_from_console() -> list[list[int]]:
    return get_numeric_matrix_from_console()


CHOOSE_INPUT_MENU_ITEMS = [
    "Ввод с клавиатуры.",
    "Случайная генерация."
]

GENERATE_MATRIX_ACTION = [
    read_numeric_matrix_from_console,
    read_random_numeric_matrix_from_console
]


def main(argv: str):
    input_type_index = read_menu_item(
        "Режим генерации матрицы:", CHOOSE_INPUT_MENU_ITEMS)

    matrix = GENERATE_MATRIX_ACTION[input_type_index]()

    print("Результат: ")
    print("Сумма элементов выше побочной диагонали:",
          sum(iterate_upper_left_triangle(matrix, False)))
    print("Сумма элементов ниже побочной диагонали:",
          sum(iterate_down_right_triangle(matrix, False)))

    return 0


if __name__ == "__main__":
    main(sys.argv)
