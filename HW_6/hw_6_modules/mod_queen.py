from random import shuffle


# Для второй задачи def is_attack() можно было сократить на две проверки,
# но пришлось бы писать отдельно функцию для первой задачи,
# выбрал оставить универсальный вариант.


def is_attack(q1, q2):
    """ Ферзи бьют друг друга, если они находятся на одной горизонтали, вертикали или диагонали
    Это значит, что x1 == x2 или y1 == y2 или |x1 - x2| == |y1 - y2|"""

    return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])


def is_valid(queens):
    """Функция проверяет, есть ли среди восьми ферзей пара бьющих друг друга"""

    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if is_attack(queens[i], queens[j]):
                return False
    unique_values(queens)
    return True


def unique_values(res):
    """Функция убирает дублирующие решения"""

    s = sorted(res)
    if s not in ls_res:
        ls_res.append(s)


def coordinates_queens():
    """Функция формирует случайные координаты расположения ферзей,
    исключая попадания их на одну горизонталь или вертикаль."""

    ls1 = [1, 2, 3, 4, 5, 6, 7, 8]
    shuffle(ls1)
    ls2 = [1, 2, 3, 4, 5, 6, 7, 8]
    shuffle(ls2)
    ls = zip(ls1, ls2)
    return list(ls)


def start_search(count_res):
    """Функция запускает поиск"""

    count_t = 0
    while count_t < count_res:
        if not is_valid(coordinates_queens()):
            continue
        else:
            count_t += 1
            is_valid(coordinates_queens())


def start_tr(count_try=4):
    """Функция запуска и вывода информации"""

    start_search(count_try)
    for i, n in enumerate(ls_res, 1):
        print(f'Вариант {i}: {n}')
    print(f'Всего решений: {len(ls_res)}')


ls_res = []
