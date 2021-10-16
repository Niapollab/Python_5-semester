import sys
import os
from typing import Iterable
from base_student_reader import BaseStudentReader
from console_student_reader import ConsoleStudentReader
from file_student_reader import FileStudentReader
from student import Student
from contractor_student import ContractorStudent
from utils import quicksort
from console_utils import *

CHOOSE_INPUT_MENU_ITEMS = [
    "Ввод с клавиатуры.",
    "Ввод из файла."
]

def main(argv):
    menu_item = read_menu_item("Выберите режим ввода: ", CHOOSE_INPUT_MENU_ITEMS)
    
    if menu_item == 0:
        reader = ConsoleStudentReader()
    elif menu_item == 1:
        print("Введите название файла: ", end='')
        filename = input()
        reader = FileStudentReader(filename)
    
    students = [*reader.enumerate_students()]
    
    if len(students) > 1:
        quicksort(students)

        print("Список студентов:")
        print(os.linesep.join(str(student) for student in students))

        first = students[0]
        second = students[1]

        print(f"Сумма: {first + second}")
        print(f"Разность: {first - second}")
        print(f"Произведение: {first * second}")
        print(f"Частное: {first / second}")

        first.to_next_course()
        second.to_next_course()

        print("Измененный список студентов:")
        print(os.linesep.join(str(student) for student in students))
    else:
        print("Студентов должно быть хотя бы 2.")
    return 0


if __name__ == "__main__":
    main(sys.argv)
