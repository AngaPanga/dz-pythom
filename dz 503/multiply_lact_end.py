# -- coding: utf-8 --
from random import*

# Случайный массив
def random_array(n = 9):
    arr = []
    for i in range (0, n):
        arr.append(randint(0, 10))
    return arr

# Произведение элементов
def multiply_element():
    array = random_array()
    print('Сгенерированный массив:\n', *array)
    result = []
    count = len(array)//2 + 1
    for i in range (0, count):
        result.append(array[i]*array[-(i+1)])
    print('Результат перемножения:\n', *result)

# Код программы
multiply_element()
input()