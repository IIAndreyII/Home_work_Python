# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# Значения не удаляются, а помещаются в одноимённые переменные без s на конце.


def change_variable():
    dict_globals = globals()
    for key, values in list(dict_globals.items()):
        if len(key) > 1 and key[-1] == 's':

            dict_globals[key[:-1]] = values
            dict_globals[key] = None


s = 54321
dsrt = 12345
r_s = 107
ads = 'eklmn'
car = 'mod'

print(f's = {s}, dsrt = {dsrt}, r_s = {r_s}, ads = {ads}, car = {car}')
change_variable()
print(f's = {s}, dsrt = {dsrt}, r_s = {r_s}, ads = {ads}, car = {car}')
print(f'r_ = {r_}, ad = {ad}')