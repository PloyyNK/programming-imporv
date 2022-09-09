"""Student Class will store student id, name, and GPA"""


class Student:

    def __init__(self, name, student_id, gpa):
        self._student_name = name
        if not isinstance(student_id, str):
            raise TypeError("Student ID must be string")
        self._student_id = student_id
        self._student_gpa = gpa

    @property
    def student_id(self):
        return self._student_id

    @property
    def student_name(self):
        return self._student_name

    @property
    def gpa(self):
        return self._student_gpa

    @gpa.setter
    def gpa(self, new_gpa):
        if not isinstance(new_gpa, float):
            raise TypeError("GPA must be float")
        self._student_gpa = new_gpa


if __name__ == "__main__":
    tony = Student("Tony Stark", "0001", 3.5)
    print(tony.student_name)
    print(tony.student_id)
    print(tony.gpa)
    tony.gpa = 4.0
    print(tony.gpa)

