import study

import random
import typing
class Teacher : pass
class Student : pass


class Group:
    def __init__(self, students: typing.List[Student]):  # field - enum class, а надо ли?
        self.students = students

    def __repr__(self):
        students = ''.join([str(i) for i in self.students])
        return f'I am group, I have {len(self.students)} students, they are: {students} '

    def add_student(self, student: Student):
        self.students.append(student)

    def drop_student(self, student: Student):
        self.students.remove(student)

    def subscr_stud_subj(self, student: Student, subject: study.Subject):
        student.subjects.append(subject)


class Department:
    def __init__(self,  teachers: typing.List[Teacher]):
        self.teachers = teachers  #зачем вообще эти поля

    def __repr__(self):
        return f'I am department, I have {len(self.teachers)} teachers'

    def appoint_teacher(self, group: Group):
        for sbj in group.subjects:
            if sbj in self.subjects:
                sbj.teacher = random.choice(self.teachers)
