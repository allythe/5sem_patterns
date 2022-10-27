import university_collaborations as uc
import factories as fct
import locations as loc
import study as s

import typing
import humans as hm


class Location:
    def __init__(self, location_type):
        print(f'I am a location, my type is:{location_type}, created!')


class University(Location):
    def __init__(self):
        super().__init__('university')

        students = fct.StudentFactory().create_n(5)
        teachers = fct.TeacherFactory().create_n(2)

        self.groups = fct.GroupFactory(students).create_n(2)
        self.departments = fct.DepartmentFactory(teachers).create_n(1)

    def __repr__(self):
        groups = '\n'.join([str(i) for i in self.groups])
        departments = '\n'.join([str(i) for i in self.departments])
        return f'I am university, I have {len(self.groups)} groups, they are: \n{groups} \nI have {len(self.departments)} departments, they are: \n{departments}'

    def start(self):
        pass


class Dormitory(Location):
    def __init__(self):
        super().__init__('dormitory')


class OuterWorld(Location):
    def __init__(self):
        super().__init__('outer world')

