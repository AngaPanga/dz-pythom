# -- coding: utf-8 --
from random import*

# Случайный массив
def random_array(n = 10):
    arr = []
    for i in range (0, n):
        arr.append(randint(-25, 25))
    return arr

# Сумма нечетных
def sum_element():
    array = random_array()
    print('Сгенерированный массив:\n', *array)
    sum = 0
    for i in range (0,len(array)):
        if i % 2 == 1:
            sum += array[i]
    print(f'Сумма элементов нечетных индексов = ', sum)

# Код программы
sum_element()
input()