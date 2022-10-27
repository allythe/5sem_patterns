import study

import random
import typing
import factories

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
        self.teachers = teachers

        subjects = factories.SubjectFactory(random.choice(self.teachers)).create_n(2)
        self.subjects = subjects

    def __repr__(self):
        subjects = '\t'.join([str(i) for i in self.subjects])
        return f'I am department, I have {len(self.teachers)} teachers, I have \n \t{subjects}'

    def appoint_teacher(self, group: Group):
        for les in group.lessons:
            if les.subject in self.subjects:
                les.subject.teacher = random.choice(self.teachers)

