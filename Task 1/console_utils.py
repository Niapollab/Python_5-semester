import os
from typing import Iterable


def clear():
    os.system("cls")


def pause():
    os.system("pause")


def print_menu(menu_name: str, menu_items: list[str]):
    print(menu_name)
    for index in range(len(menu_items)):
        print(index + 1, menu_items[index], sep='. ')


def read_menu_item(menu_name: str, menu_items: list[str]) -> int:
    while True:
        clear()
        print_menu(menu_name, menu_items)
        print("Выберите номер пункта меню: ", end='')
        user_input = input()
        index = int(user_input) if user_input.isnumeric() else None
        if index is None or index < 1 or index > len(menu_items):
            print("Не удалось распознать пункт меню. Повторите попытку ввода.")
            pause()
        else:
            break
    return index - 1


def safe_int_input(input_text: str = "Введите целочисленное значение: ", error_message: str = "Не удалось распознать целочисленное значение.") -> int:
    while True:
        print(input_text, end='')
        result = input()
        if result.isnumeric():
            return int(result)
        print(error_message)


def enumerate_lines_from_console() -> Iterable[str]:
    while True:
        s = input()
        if not s:
            break
        yield s


def get_numeric_matrix_from_console(input_text: str = "Введите целочисленную матрицу:", error_message: str = "Не удалось распознать матрицу.") -> list[list[int]]:
    while True:
        print(input_text)
        str_matrix = [line.split(' ')
                      for line in enumerate_lines_from_console()]
        all_is_numeric = all(all(cell.isnumeric()
                             for cell in row) for row in str_matrix)
        is_rectangular_2d_array = True if len(
            set(len(row) for row in str_matrix)) == 1 else False
        if all_is_numeric and is_rectangular_2d_array:
            return [[int(cell) for cell in row] for row in str_matrix]
        print(error_message)
