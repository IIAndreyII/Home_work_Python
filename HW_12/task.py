# Создайте класс студента.
# * Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# * Названия предметов должны загружаться из файла CSV при создании экземпляра.
#   Другие предметы в экземпляре недопустимы.
# * Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# * Также экземпляр должен сообщать средний балл по тестам
#   для каждого предмета и по оценкам всех предметов вместе взятых.

import csv
import copy


class CheckingLetters:
    """Дескриптор для проверки слова."""

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        return setattr(instance, self.param_name, value)

    def validate(self, value):
        if not value.isalpha() or not value.istitle():
            raise ValueError(f'"{value}"должно начинаться с заглавной буквы и состоять только из букв')


class Range:
    """Дескриптор для проверки диапазона и значения на целое число"""

    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        return setattr(instance, self.param_name, value)

    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError(f'{value} должно быть целым числом')
        if value > self.max_value or value < self.min_value:
            raise ValueError(f'должно быть в диапазоне от {self.min_value} до {self.max_value}')


class Theme:
    """Класс Предмет"""

    def __init__(self, name, list_res_tests=None):
        self._name = name
        self.list_res_tests = list_res_tests

    @property
    def name(self):
        return self._name

    @property
    def get_theme(self):
        return [self.name] + self.list_res_tests

    def __str__(self) -> str:
        return f"Предмет: {self.name}, результаты тестов: {self.list_res_tests}"


class Themes:
    """Класс имеет атрибут 'file' с именем файла с информацией и
    создаваемые атрибуты, содержащие класс 'Theme'."""

    def __init__(self, file):
        self.file = file
        with open(self.file, "r", encoding="utf-8", newline='') as f:
            csv_file = csv.reader(f)
            for line in csv_file:
                theme = line[0]
                setattr(self, theme, Theme(theme, line[1:]))

class Student:
    """Класс Студент"""
    family = CheckingLetters()
    first_name = CheckingLetters()
    last_name = CheckingLetters()
    evaluations = Range(2, 5)   # количество оценок от 2 до 5
    res_test = Range(0, 100)   # результат теста от 0 до 100

    def __init__(self, family, name, patronymic, file):
        self.family = family
        self.name = name
        self.patronymic = patronymic
        self.file = file
        self.__themes = Themes(self.file)

    def add_res_test(self, theme, number):
        """Добавление результата теста в предмет"""
        obj_theme = getattr(self.__themes, theme)
        old_count_tests = len(obj_theme.list_res_tests)
        self.count_tests = old_count_tests + 1
        self.res_test = number
        obj_theme.list_res_tests.append(self.res_test)
        with open(self.file, "w", encoding="utf-8", newline='') as f:
            csv_write = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
            all_data = []
            for key in self.__themes.__dict__.keys():
                if key == "file":
                    continue
                obj_theme = getattr(self.__themes, key)
                all_data.append(obj_theme.get_theme)
            csv_write.writerows(all_data)


    def average_by_theme(self, theme):
        """Средний балл"""
        obj_theme = getattr(self.__themes, theme)
        temp = obj_theme.list_res_tests
        average = round(sum(map(int, temp)) / len(temp), 1)
        return average

    def average_by_themes(self):
        """Средний балл по тестам для всех предметов"""
        themes_dict = copy.deepcopy(self.__themes.__dict__)
        del themes_dict["file"]
        temp_list = []
        for value in themes_dict.values():
            temp_list = temp_list + value.list_res_tests
        average = round(sum(map(int, temp_list)) / len(temp_list), 1)
        return average

    def __repr__(self) -> str:
        return f"Student({self.family}, {self.name}, {self.patronymic}, {self.file})"


st_1 = Student("Петров", "Петр", "Петрович", "academic_subjects.csv")
print(st_1)

print(f'Средний балл по Математике = {st_1.average_by_theme("Математика")}')
print(f'Средний балл по Физике = {st_1.average_by_theme("Физика")}')
print(f'Средний балл по Химии = {st_1.average_by_theme("Химия")}')
print(f'Средний балл по всем предметам = {st_1.average_by_themes()}')

