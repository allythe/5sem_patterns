class Human:
    def __init__(self, name, age, mood, current_building, health_points):
        self.name = name
        self.age = age
        self.mood = mood
        self.cur_building = current_building
        self.hp = health_points

    def eat(self):
        pass

    def sleep(self):
        pass

    def go(self):
        pass

class EducationalHuman(Human):
    def notify(self):
        pass

    def leave_institute(self):
        if self.cur_building == "institute":
            self.cur_building = "dormitory"

class Student(EducationalHuman):
    def __init__(self, name, age, mood, current_building, health_points, subjects):
        EducationalHuman.__init__(self, name, age, mood, current_building, health_points)
        self.subjects = subjects

    def botay(self):
        pass

    def katay(self):
        pass

    def get_task(self):
        pass

    def check_state(self):
        pass

class Teacher(EducationalHuman):
    def __init__(self, name, age, mood, current_building, health_points, subjects):
        EducationalHuman.__init__(self, name, age, mood, current_building, health_points)
        self.subjects = subjects