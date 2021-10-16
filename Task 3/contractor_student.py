from student import Student


class ContractorStudent(Student):
    def __init__(self, fullname: str, faculty: str, course: int, min_mark: int, is_contract_paid: bool) -> None:
        super().__init__(fullname, faculty, course, min_mark)
        self.__is_contract_paid = is_contract_paid

    @property
    def is_contract_paid(self) -> bool:
        return self.__is_contract_paid

    @property
    def scholarship(self) -> int:
        return 0

    def to_next_course(self) -> bool:
        return self.__is_contract_paid and super().to_next_course()
