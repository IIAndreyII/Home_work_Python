# Создайте функцию генератор чисел Фибоначчи (см. Википедию)

def fibonacci():
    fib_1 = 1
    fib_2 = 1
    while True:
        fib_sum = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = fib_sum
        yield fib_sum


for n, fib in enumerate(fibonacci(), start=1):
    print(fib)
    if n == 10:
        break
