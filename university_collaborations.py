from humans import Student, Teacher
from study import  Subject

import typing


class Group:
    def __init__(self, students: typing.List[Student], subjects: typing.List[Subject], field: str, teachers: typing.List[Teacher], course : int):
        self.students = students
        self.subjects = subjects

        self.field = field
        if course > 10 | course < 1:
            RuntimeError('Invalid course number, it should be between 1 and 10')

        self.course = course
        self.teachers = teachers

    def get_field(self):
        return self.field

    def get_course(self):
        return self.course

    def add_student(self, student:Student):
        self.students.append(student)

    def drop_student(self, student:Student):
        self.students.remove(student)

    def subscr_stud_subj(self, student:Student, subject:Subject):
        student.subjects.append(subject)


class Department:
    def __init__(self, ):
        pass





