from abc import ABC, abstractmethod
from typing import Iterable
from student import Student


class BaseStudentReader(ABC):
    @abstractmethod
    def read_student(self) -> Student | None:
        pass

    def enumerate_students(self) -> Iterable[Student]:
        student = self.read_student()
        while student != None:
            yield student
            student = self.read_student()
