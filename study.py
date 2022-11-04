import typing
import factories as fct

#import humans
import datetime

class Teacher: pass


class Task:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def __repr__(self):
        return f'I am a task, my name is {self.name} \n'

    def do(self):
        pass

    def check(self):
        pass

    def submit(self):
        pass


class Subject: #откуда предмет знает свой семестр или тау 4 семестра и тау 5 семестра это тупо разные предметы
    def __init__(self, teacher: Teacher, course = 1, tasks: typing.List[Task] = None):
        self.teacher = teacher
        self.course = course
        self.name == __class__.__name__
        self.tasks = fct.TasksFactory(self).create_n(1)

    def __repr__(self):
        tasks = '\n'.join([str(i) for i in self.tasks])
        return f'I am a subject, my name is: {self.name}\n \t\t my teacher is {str(self.teacher)} \n \tI have {len(self.tasks)} tasks, they are: \n \t\t {tasks}'


class Math(Subject):
    def __init__(self, teacher: Teacher, course = 1, tasks: typing.List[Task] = None):
        self.name = "Mathematics"
        super().__init__(teacher, course, tasks)


class Physics(Subject):
    def __init__(self, teacher: Teacher, course=1, tasks: typing.List[Task] = None):
        self.name = "Physics"
        super().__init__(teacher, course, tasks)


class Lesson:
    def __init__(self, room: int, students, subject: Subject, time: datetime, teacher: Teacher):
        self.room = room
        self.teacher = teacher
        self.students = students
        self.subject = subject
        self.time = time