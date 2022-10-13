from locations import Location

MAX_HP = 100


class Human:
    def __init__(self, name, age, mood, cur_location, health_points):
        self.name = name
        self.age = age
        self.mood = mood
        self.cur_location = cur_location
        self.hp = health_points

    def __call__(self, *args, **kwargs):
        print(f'I am {self.name}, my age is {self.age}, I am in {self.cur_location}, mood: {self.mood}, hp: {self.hp}')

    def eat(self):
        self.hp = MAX_HP

    def sleep(self):
        self.hp = MAX_HP

    def go(self, location: Location):
        self.cur_location = location
        self.hp -= 10


class EducationalHuman(Human):
    def notify(self):
        pass

    def leave_institute(self):
        pass


class Student(EducationalHuman):
    def __init__(self, name, age, mood, current_building, health_points, subjects):
        super().__init__(self, name, age, mood, current_building, health_points)
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
        super().__init__(self, name, age, mood, current_building, health_points)
        self.subjects = subjects
