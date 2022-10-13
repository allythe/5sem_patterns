import typing

from humans import Student
import datetime


class Task:
    def __init__(self):
        pass

    def do(self):
        pass

    def check(self):
        pass

    def submit(self):
        pass


class Subject:
    def __init__(self, tasks : typing.List[Task]):
        self.tasks = tasks


class Lesson:
    def __init__(self, room: int, students: typing.List[Student], subject: Subject, time: datetime):
        self.room = room
        self.students = students
        self.subject = subject
        self.time = time