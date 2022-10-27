import typing
import factories as fct

#import humans
import datetime

class Teacher: pass


class Task:
    def __init__(self, name):
        self.name = name
        pass

    def __repr__(self):
        return f'I am a task, my name is {self.name} \n'

    def do(self):
        pass

    def check(self):
        pass

    def submit(self):
        pass

    @staticmethod
    def random_name():
        name = 'Math'
        return name


class Subject: #откуда предмет знает свой семестр или тау 4 семестра и тау 5 семестра это тупо разные предметы
    def __init__(self, teacher: Teacher, tasks: typing.List[Task] = None):
        self.teacher = teacher
        tasks = fct.TasksFactory().create_n(1)
        self.tasks = tasks

    def __repr__(self):
        tasks = '\n'.join([str(i) for i in self.tasks])
        return f'I am a subject,\n \t\t my teacher is {str(self.teacher)} \n \tI have {len(self.tasks)} tasks, they are: \n \t\t {tasks}'


class Lesson:
    def __init__(self, room: int, students, subject: Subject, time: datetime, teacher: Teacher):
        self.room = room
        self.teacher = teacher
        self.students = students
        self.subject = subject
        self.time = time