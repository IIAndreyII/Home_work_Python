# 2.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину
# каждого отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок
# окажется больше суммы двух других, то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.


a, b, c = map(int, input('Введите, длины сторон треугольника, через пробел =>>> ').split())

res = ''
if (a < b + c) and (b < a + c) and (c < a + b):
    if a == b == c:
        res = 'Треугольник равносторонний.'
    elif (a == b) or (a == c) or (b == c):
        res = 'Треугольник равнобедренный.'
    else:
        res = 'Треугольник разносторонний.'
else:
    res = 'Такой треугольник не существует.'

print(res)