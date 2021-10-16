from __future__ import annotations


class Student:
    MIN_MARK_FOR_NEXT_COURSE = 3
    MAX_ACCESSIBLE_COURSE = 4
    SCHOLARSHIP_SIZE = {
        5: 300,
        4: 200
    }

    def __init__(self, fullname: str, faculty: str, course: int, min_mark: int) -> None:
        self.__fullname = fullname
        self.__faculty = faculty
        self.__course = course
        self.__min_mark = min_mark

    @property
    def fullname(self) -> str:
        return self.__fullname

    @property
    def faculty(self) -> str:
        return self.__faculty

    @property
    def course(self) -> int:
        return self.__course

    @property
    def min_mark(self) -> int:
        return self.__min_mark

    @property
    def scholarship(self) -> int:
        for element in Student.SCHOLARSHIP_SIZE:
            if self.__min_mark >= element:
                return Student.SCHOLARSHIP_SIZE[element]
        return 0

    def to_next_course(self) -> bool:
        if self.__course <= Student.MAX_ACCESSIBLE_COURSE and self.__min_mark >= Student.MIN_MARK_FOR_NEXT_COURSE:
            self.__course += 1
            return True
        return False

    def __add__(self, other: int) -> Student:
        new_min_mark = self.__min_mark + other
        return Student(self.__fullname, self.__faculty, self.__course, new_min_mark)

    def __sub__(self, other: int) -> Student:
        new_min_mark = self.__min_mark - other
        return Student(self.__fullname, self.__faculty, self.__course, new_min_mark)

    def __mul__(self, other: int) -> Student:
        new_min_mark = self.__min_mark * other
        return Student(self.__fullname, self.__faculty, self.__course, new_min_mark)

    def __truediv__(self, other: int) -> Student:
        new_min_mark = self.__min_mark / other
        return Student(self.__fullname, self.__faculty, self.__course, new_min_mark)

    def __radd__(self, other: int) -> int:
        return self.__min_mark + other

    def __rsub__(self, other: int) -> int:
        return self.__min_mark - other

    def __rmul__(self, other: int) -> int:
        return self.__min_mark * other

    def __rtruediv__(self, other: int) -> int:
        return self.__min_mark / other

    def __iadd__(self, other: int) -> Student:
        self.__min_mark += other
        return self

    def __isub__(self, other: int) -> Student:
        self.__min_mark -= other
        return self

    def __imul__(self, other: int) -> Student:
        self.__min_mark *= other
        return self

    def __itruediv__(self, other: int) -> Student:
        self.__min_mark //= other
        return self

    def __eq__(self, other: Student) -> bool:
        return other != None and self.__min_mark == other.__min_mark

    def __lt__(self, other: Student) -> bool:
        return self.__min_mark < other.__min_mark

    def __ne__(self, other: Student) -> bool:
        return not (self == other)

    def __le__(self, other: Student) -> bool:
        return self == other or self < other

    def __gt__(self, other: Student) -> bool:
        return not (self <= other)

    def __ge__(self, other: Student) -> bool:
        return not (self < other)

    def __str__(self) -> str:
        return f"Студент {self.__fullname} факультета {self.__faculty} {self.__course}-го курса имеющий {self.__min_mark}-ку в качестве минимальной оценки и получающий {self.scholarship} в качестве стипендии."
