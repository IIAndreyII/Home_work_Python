# 5. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код:
# --- from random import randint ---
# --- num = randint(LOWER_LIMIT, UPPER_LIMIT) ---


from random import randint

count = 10
num_bot = randint(0, 1000)

while count > 0:
    num_use = int(input('Введите число: '))
    count -= 1
    if num_bot == num_use:
        print('Вы выиграли!!!')
        break
    elif num_bot > num_use:
        print(f'Ваше число меньше, осталось попыток: {count}')
    else:
        print(f'Ваше число больше, осталось попыток: {count}')

print('Вы использовали все попытки.')
