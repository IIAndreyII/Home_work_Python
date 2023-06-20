# 1.Решить задачи, которые не успели решить на семинаре.
# Задание №9
# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.


start_row = 2
start_column = 2
column = 9 + 1
rows = 10 + 1
first_line = column // 2 + 1

for i in range(start_row, rows):
    print()
    for j in range(start_column, first_line):
        print(f'{j:>2}  X {i:>2} = {i * j:>2}', end='      ')
print()
for i in range(start_row, rows):
    print()
    for j in range(first_line, column):
        print(f'{j:>2}  X {i:>2} = {i * j:>2}', end='      ')
