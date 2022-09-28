# -- Coding: utf-8 --

# Поиск множителей
def find_multipliers(n):
    if n < 0:
        n = -n
    if n == 0:
        print('Множители числа 0 = 0')
    else:
        array = []
        for i in range(1, n+1):
            if n % i == 0:
                array.append(i)
        print(f'Множители числа {n}: ', *array)

# Код программы
number = int (input('Введите число: '))
find_multipliers(number)