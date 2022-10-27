import humans as hm
import university_collaborations as uc
import study as st


class Factory:
    def __init__(self):
        pass

    def create(self):
        pass

    def create_n(self, n):
        tmp = []
        for i in range(n):
            tmp.append(self.create())
        return tmp


class StudentFactory(Factory):
    def __init__(self):
        super().__init__()

    def create(self):
        return hm.Student(hm.Human.random_name(), hm.Human.random_age())


class GroupFactory(Factory):
    def __init__(self, students):
        super().__init__()
        self.students = students

    def create(self, students):
        return uc.Group(students)

    def create_n(self, n):
        return [self.create(self.students[len(self.students)//n*i:len(self.students)//n*(i+1)]) for i in range(n)]


class DepartmentFactory(Factory):
    def __init__(self, teachers):
        super().__init__()
        self.teachers = teachers

    def create(self):
        return uc.Department(self.teachers)


class TeacherFactory(Factory):
    def create(self):
        return hm.Teacher(hm.Human.random_name(), hm.Human.random_age())


class SubjectFactory(Factory):
    def __init__(self, teacher):
        super().__init__()
        self.teacher = teacher

    def create(self):
        return st.Subject(self.teacher)


class TasksFactory(Factory):
    def create(self):
        return st.Task(st.Task.random_name())

