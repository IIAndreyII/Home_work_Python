#  Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.

data_list = [1, 2, 22, 3, 33, 4, 44, 2, 22, 2, 4, 44, 5]
res_list = []
for i in data_list:
    if data_list.count(i) > 1 and i not in res_list:
        res_list.append(i)
print(res_list)
