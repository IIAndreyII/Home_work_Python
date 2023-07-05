# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

from os.path import splitext, basename, dirname


def split_path(s):
    return dirname(s), splitext(basename(s))[0], splitext(s)[1][1:]


absolute_path = "E:\Обучение\Курсы\Погружение в Python (семинары)\Урок 5. Интераторы и генераторы\HW5\paint.bmp"
print(split_path(absolute_path))
