# Задание №3
# Создайте класс с базовым исключением и дочерние классы исключения:
# ○ ошибка уровня,
# ○ ошибка доступа.


class MyExceptionGlob(Exception):
    pass


class MyExceptionErrorLevel(MyExceptionGlob):
    def __init__(self, level_min, level_max):
        self.level_min = level_min
        self.level_max = level_max

    def __str__(self):
        return f'Уровень доступа пользователя не входит в интервал от {self.level_min} до {self.level_max}'


class MyExceptionErrorAccess(MyExceptionGlob):
    def __init__(self, u_name, u_id):
        self.u_name = u_name
        self.u_id = u_id

    def __str__(self):
        return f'Пользователь {self.u_name} с id "{self.u_id}" не имеет доступа к системе'


class MyExceptionErrorAdmLevel(MyExceptionGlob):
    def __init__(self, u_level):
        self.u_level = u_level

    def __str__(self):
        return f'Пользователь ниже уровня доступа "{self.u_level}" не имеет прав на модификации'
