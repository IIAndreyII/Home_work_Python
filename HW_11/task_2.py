# Создайте класс Матрица. Добавьте методы для: вывода на печать,
# проверку на равенство, сложения, *умножения матриц


class Matrix:
    """Класс Матрица"""

    def __init__(self, matrix):
        self.matrix = matrix
        self.len_matr = len(matrix)


    def get_matrix(self):
        return self.matrix

    def __add__(self, other):
        """Сложение матриц. Складывает соответствующие элементы двух матриц
        и заносит результат в итоговую матрицу"""

        if self.len_matr != other.len_matr:
            return f'Ошибка: матрицы разных размеров'
        for i in range(len(self.matrix)):
            if len(self.matrix[i]) != len(other.matrix[i]):
                return f'Ошибка: матрицы разных размеров'
        Matrix = []
        for i in range(len(self.matrix)):
            Matrix.append([self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[i]))])
        return Matrix

    def __mul__(self, other):
        """Произведение матриц. Для того, чтобы найти произведение матриц нужно
        строки первой матрицы умножить на столбцы второй матрицы."""

        if len(self.matrix[0]) != len(other.matrix):
            return f'Ошибка: нельзя перемножить данные матрицы'
        Matrix = []
        for i_row in self.matrix:
            Matrix.append([sum(i * j for i, j in zip(i_row, j_col)) for j_col in zip(*other.matrix)])
        return Matrix

    def __eq__(self, other):
        if self.len_matr != other.len_matr:
            return f'Ошибка: матрицы разных размеров'
        for i in range(len(self.matrix)):
            if len(self.matrix[i]) != len(other.matrix[i]):
                return f'Ошибка: матрицы разных размеров'
        else:
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    if self.matrix[i][j] != other.matrix[i][j]:
                        return False
            return True

    def __str__(self):
        return '\n'.join(map(str, self.matrix))


matrix_1 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [10, 11, 12]]

matrix_2 = [[13, 14, 15],
            [16, 17, 18],
            [19, 20, 21],
            [22, 23, 24]]

matrix_3 = [[24, 23, 22, 21],
            [20, 19, 18, 17],
            [16, 15, 14, 13]]

matrix_4 = [[12, 11, 10, 9, 8],
            [7, 6, 5, 4, 3],
            [2, 1, 0, -1, 0]]

matrix_1 = Matrix(matrix_1)
matrix_2 = Matrix(matrix_2)
matrix_3 = Matrix(matrix_3)
matrix_4 = Matrix(matrix_4)

print("Cложение матриц:")
matrix_sum = matrix_1 + matrix_2
print(matrix_sum)

print("Умножение матриц:")
matrix_mul = matrix_1 * matrix_3
print(matrix_mul)
print(matrix_1 * matrix_4)

print("Cравнение матриц:")
print(matrix_1 == matrix_2)
