import typing

#import humans
import datetime

class Teacher: pass


class Task:
    def __init__(self):
        pass

    def do(self):
        pass

    def check(self):
        pass

    def submit(self):
        pass


class Subject: #откуда предмет знает свой семестр или тау 4 семестра и тау 5 семестра это тупо разные предметы
    def __init__(self, tasks: typing.List[Task], teacher : Teacher):
        self.tasks = tasks
        self.teacher = teacher


class Lesson:
    def __init__(self, room: int, students, subject: Subject, time: datetime):
        self.room = room
        self.students = students
        self.subject = subject
        self.time = time