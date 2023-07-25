import csv
from random import randint


def generate_csv(path):
    """
    Генерация csv файла с тремя случайными числами в каждой строке.
    100-1000 строк.
    """
    with open(path, 'w', encoding='utf-8', newline='') as c:
        csv_writer = csv.writer(c)
        csv_writer.writerow(['a', 'b', 'c'])
        lines = randint(100, 1000)
        for _ in range(lines):
            csv_writer.writerow([randint(0, 1000), randint(0, 1000), randint(0, 1000)])