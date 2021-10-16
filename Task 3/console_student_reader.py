from base_student_reader import BaseStudentReader
from student import Student
from contractor_student import ContractorStudent

class ConsoleStudentReader(BaseStudentReader):
    def __init__(self) -> None:
        self.__readed_count = 0

    def read_student(self) -> Student | None:
        print(f"Введите студента №{self.__readed_count + 1}:")

        print("ФИО (или Enter, для прекращения ввода): ", end='')
        fullname = input()
        if not fullname:
            return None

        print("Факультет: ", end='')
        faculty = input()

        course = ConsoleStudentReader.__read_course()
        min_mark = ConsoleStudentReader.__read_min_mark()
        contractor = ConsoleStudentReader.__read_is_contractor()

        self.__readed_count += 1
        
        if contractor:
            is_contract_paid = ConsoleStudentReader.__read_is_contract_paid()
            return ContractorStudent(fullname, faculty, course, min_mark, is_contract_paid)
        else:
            return Student(fullname, faculty, course, min_mark)

    @staticmethod
    def __read_is_contract_paid() -> bool:
        while True:
            print("Оплатил ли студент контракт: ", end='')
            is_contract = ConsoleStudentReader.__cast_answer_to_bool(input())
            if is_contract != None:
                return is_contract
            print("Не удалось распознать статус оплаты контракта.")

    @staticmethod
    def __read_is_contractor() -> bool:
        while True:
            print("Является ли студент контрактником: ", end='')
            is_contract = ConsoleStudentReader.__cast_answer_to_bool(input())
            if is_contract != None:
                return is_contract
            print("Не удалось распознать статус студента.")

    @staticmethod
    def __cast_answer_to_bool(answer: str) -> bool | None:
        answer = answer.lower().strip()
        if answer == "yes" or answer == "да" or answer == "+":
            return True
        if answer == "no" or answer == "нет" or answer == "-":
            return False
        return None

    @staticmethod
    def __read_course() -> int:
        while True:
            print("Курс: ", end='')
            raw_course = input()
            if raw_course.isdigit():
                course = int(raw_course)
                if course > 0 and course <= Student.MAX_ACCESSIBLE_COURSE:
                    return course
            print("Не удалось распознать номер курса.")

    @staticmethod
    def __read_min_mark() -> int:
        while True:
            print("Минимальная оценка: ", end='')
            raw_mark = input()
            if raw_mark.isdigit():
                mark = int(raw_mark)
                if mark > 1 and mark <= 5:
                    return mark
            print("Не удалось распознать оценку.")
