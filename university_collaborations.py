import study as st

import random
import typing
import factories

class Teacher : pass
class Student : pass


class Group:
    def __init__(self, students: typing.List[Student]):  # field - enum class, а надо ли?
        self.students = students
        self.subjects = None

    def __repr__(self):
        students = ''.join([str(i) for i in self.students])
        subjects = ''.join([str(i) for i in self.subjects])

        return f'I am group, I have {len(self.students)} students, they are: {students} \n ' \
               f'I have {len(self.subjects)} subjects: they are {subjects}'

    def set_subjects(self, subjects):
        self.subjects = subjects

    def add_student(self, student: Student):
        self.students.append(student)

    def drop_student(self, student: Student):
        self.students.remove(student)

    def subscr_stud_subj(self, student: Student, subject: st.Subject):
        student.subjects.append(subject)


class Department:
    def __init__(self,  teachers: typing.List[Teacher]):
        self.teachers = teachers
        self.math_factory = factories.SubjectFactory(self.teachers, st.Math)
        self.phys_factory = factories.SubjectFactory(self.teachers, st.Physics)

        self.subjects = self.math_factory.create_n(2)
        self.subjects.append(self.phys_factory.create())

    def get_subject(self):
        return random.choice(self.subjects)

    def get_subjects(self, n):
        return [self.get_subject() for i in range(n)]

    def __repr__(self):
        subjects = '\t'.join([str(i) for i in self.subjects])
        return f'I am department, I have {len(self.teachers)} teachers, I have \n \t{subjects}'

    def appoint_teacher(self, group: Group):
        for les in group.lessons:
            if les.subject in self.subjects:
                les.subject.teacher = random.choice(self.teachers)


class MathDepartment(Department):
    def __init__(self, teachers: typing.List[Teacher]):
        self.teachers = teachers
        self.math_factory = factories.SubjectFactory(self.teachers, st.Math)
        self.angem_factory = factories.SubjectFactory(self.teachers, st.Angem)

        self.subjects = self.math_factory.create_n(2)
        self.subjects.append(self.angem_factory.create())
