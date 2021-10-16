from base_student_reader import BaseStudentReader
from student import Student
from contractor_student import ContractorStudent


class FileStudentReader(BaseStudentReader):
    def __init__(self, filename: str) -> None:
        self.__file = open(filename, 'r', encoding="utf-8")

    def read_student(self) -> Student | None:
        try:
            fullname = self.__file.readline().strip()
            faculty = self.__file.readline().strip()

            if not fullname or not faculty:
                raise Exception()

            course = int(self.__file.readline().strip())
            if course < 1 or course > Student.MAX_ACCESSIBLE_COURSE:
                raise Exception()

            min_mark = int(self.__file.readline().strip())
            if min_mark < 1 or min_mark > 5:
                raise Exception()

            is_contract_paid = FileStudentReader.__cast_answer_to_bool(
                self.__file.readline().strip())

            if is_contract_paid != None:
                return ContractorStudent(fullname, faculty, course, min_mark, is_contract_paid)
            else:
                return Student(fullname, faculty, course, min_mark)
        except:
            return None

    def __exit__(self):
        if self.__file:
            self.__file.close()

    @staticmethod
    def __cast_answer_to_bool(answer: str) -> bool | None:
        answer = answer.lower().strip()
        if answer == "yes" or answer == "да" or answer == "+":
            return True
        if answer == "no" or answer == "нет" or answer == "-":
            return False
        return None
