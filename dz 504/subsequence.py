# -- coding: utf-8 --
from random import*

# Случайный массив
def random_array(n):
    arr = []
    for i in range (2*n):
        arr.append(randint(0, n))
    return arr

# Функциия отсева повторяющихся элементов
def convert_in_subsequence (num):
    original = random_array(num)
    print('Сгенерирован следующий массив элементов:\n', *original)
    result = set(original)
    print('Список состоит из следующих значений:\n',*result)

# Код программы
number = int (input('Введите число: '))
convert_in_subsequence (number)
input()