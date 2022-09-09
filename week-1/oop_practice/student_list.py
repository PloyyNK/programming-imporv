""""This class will store a list of students"""

from student import Student


class StudentList:

    def __init__(self):
        self._students_list = []

    @property
    def student_list(self):
        name_list = []
        for student in self._students_list:
            name_list.append(student.student_name)
        return name_list

    def add_student(self, student):
        if not isinstance(student, Student):
            raise TypeError("Only Student type can be store")
        self._students_list.append(student)

    def remove_student(self, student_id):
        for student in self._students_list:
            if student.student_id == student_id:
                self._students_list.remove(student)


if __name__ == "__main__":
    tony = Student("Tony Stark", "0001", 3.5)
    nat = Student("Natasha Romanov", "0002", 3.5)
    lst = StudentList()
    lst.add_student(tony)
    lst.add_student(nat)
    print(lst.student_list)
    lst.remove_student("0001")
    print(lst.student_list)

