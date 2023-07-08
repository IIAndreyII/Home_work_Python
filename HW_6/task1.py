# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код,
# решающий задачу о 8 ферзях. Известно, что на доске 8×8 можно расставить 8 ферзей так,
# чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите,
# есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину,
# а если бьют - ложь.

# from random import randint
from hw_6_modules import mod_queen

# Заданная позиция
a = [(5, 5), (1, 5), (6, 8), (5, 4), (7, 3), (8, 3), (7, 6), (4, 8)]
print(*a)
print(mod_queen.is_valid(a))

# # Получаем 8 уникальных позиций для ферзей.
# s = set()
# while len(s) < 8:
#     n = (randint(1, 8), randint(1, 8))
#     s.add(n)
# s = list(s)
# print(*s)
# print(task1_queen.is_valid(s))
