import json
from MyExceptions import MyExceptionErrorLevel


class LevelDescriptor:
    def __init__(self, level_min, level_max):
        self.level_min = level_min
        self.level_max = level_max

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if value is not None and value not in range(self.level_min, self.level_max):
            raise MyExceptionErrorLevel(self.level_min, self.level_max)
        setattr(instance, self.param_name, value)


class User:
    u_level = LevelDescriptor(1, 7 + 1)

    def __init__(self, u_name, u_id, u_level=None):
        self.u_name = u_name
        self.u_id = u_id
        self.u_level = u_level

    def __eq__(self, other):
        return self.u_name == other.u_name and self.u_id == other.u_id

    def __repr__(self):
        return f'{self.u_level = } {self.u_id = } {self.u_name = }'

    def __str__(self):
        return f'claSS User(): lev - {self.u_level}, id - {self.u_id}, name - {self.u_name}'
