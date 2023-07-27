# 1. Доработаем задачи 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.


class Cat:
    def __init__(self, name, param):
        self.name = name
        self.param = param


class Dog:
    def __init__(self, name, param):
        self.name = name
        self.param = param


class Birds:
    def __init__(self, name, param):
        self.name = name
        self.param = param


class Factory(Cat, Dog, Birds):
    def __init__(self, class_name, name, param):
        super().__init__(name, param)
        self.__class__ = class_name


cat_1 = Cat('Tom', 123)
cat_2 = Factory(Cat, 'Tom_2', 444)
dog_1 = Dog('Rex', 546)
dog_2 = Factory(Dog, 'Rex_2', 897)
bird_1 = Birds('Kar', '345')
bird_2 = Factory(Birds, 'Kar_2', 765)

print(type(cat_1), cat_1.name, cat_1.param)
print(type(cat_2), cat_2.name, cat_2.param)
print(type(dog_1), dog_1.name, dog_1.param)
print(type(dog_2), dog_2.name, dog_2.param)
print(type(bird_1), bird_1.name, bird_1.param)
print(type(bird_2), bird_2.name, bird_2.param)
