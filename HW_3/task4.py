# 4. Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.

from itertools import combinations

thingth = {
    'палатка': 5,
    'спальник': 2,
    'еда': 10,
    'вода': 10,
    'дрова': 20,
    'посуда': 5,
    'котелок': 2,
    'нож': 0.2,
    'спички': 0.02,
    'топор': 2,
    'фонарик': 0.5
}

MAX_WEIGHT_THINGS = 20

res = []

for i in range(len(thingth)):
    temp = []
    items_combinations = combinations(thingth, i)
    for combination in items_combinations:
        temp_dict = thingth.copy()
        weight = 0
        for item in combination:
            weight += thingth[item]
            temp_dict.pop(item)
        if weight <= MAX_WEIGHT_THINGS:
            min_weight_item = min(temp_dict.items(), key=lambda x: x[1])
            if weight + min_weight_item[1] <= MAX_WEIGHT_THINGS:
                continue
            else:
                res.append(list(combination) + [weight])
for res1 in res:
    print(res1)
