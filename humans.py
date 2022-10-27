import locations

MAX_HP = 100


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.mood = 100
        self.cur_location = None
        self.hp = 100

    def __repr__(self):
        return f' {self.name}, {self.age}'

    def __call__(self):
        print(f'I am {self.name}, my age is {self.age}, I am in {self.cur_location}, mood: {self.mood}, hp: {self.hp}')

    def eat(self):
        self.hp = MAX_HP

    def sleep(self):
        self.hp = MAX_HP

    def go(self, location: locations.Location):
        self.cur_location = location
        self.hp -= 10

    @staticmethod
    def random_name():
        name = 'Arina'
        return name

    @staticmethod
    def random_age():
        age = -17
        return age


class EducationalHuman(Human):
    def notify(self):
        pass

    def leave_institute(self):
        pass


class Student(EducationalHuman):

    def botay(self):
        pass

    def katay(self):
        pass

    def get_task(self):
        pass

    def check_state(self):
        pass


class Teacher(EducationalHuman):
    def __init__(self, name, age, subjects = None):
        super().__init__(name, age)
        self.subjects = subjects

# teachers, departements creator (factory)