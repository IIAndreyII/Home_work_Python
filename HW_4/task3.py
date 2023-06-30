# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем,
# используйте его строковое представление.


def reverse_key_values(**kwargs):
    temp = {}
    for key, value in kwargs.items():
        if not isinstance(value, str):
            value = str(value)
        temp[value] = key
    return temp


print(reverse_key_values(a=[150, 500, -200], b=500, c=(500, -200), d='abcd'))
