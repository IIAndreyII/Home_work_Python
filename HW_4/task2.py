# Напишите функцию для транспонирования матрицы


def transpositions_matr(matr):
    matr_temp = []
    for i in zip(*matr):
        matr_temp.append(list(i))
    return matr_temp


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(matrix)
print(transpositions_matr(matrix))
