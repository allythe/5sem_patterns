from university_collaborations import Department, Group

import typing


class Location:
    def __init__(self, location_type):
        print(f'I am a location, my type is:{location_type}, created!')


class University(Location):
    def __init__(self, departments: typing.List[Department], groups: typing.List[Group]):
        super().__init__('university')
        self.departments = departments
        self.groups = groups

    def add_group(self, group:Group):
        self.groups.append(group)

    def drop_group(self, group:Group):
        self.groups.remove(group)


class Dormitory(Location):
    def __init__(self):
        super().__init__('dormitory')


class OuterWorld(Location):
    def __init__(self):
        super().__init__('outer world')




