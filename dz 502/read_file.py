# -- coding: utf-8 --
from random import*

# Считывание с файла
def read_file():
    with open("index.txt", "r") as file:
        arr_i = file.readlines()
    file.close()
    return arr_i

# Случайный массив
def random_array(n):
    arr = []
    for i in range (0, n):
        arr.append(randint(-n, n))
    return arr

# Код программы
n = int(input('Введите число элементов: '))
index_array = read_file()
new_rand_array = random_array(n)
print (*new_rand_array, '\n Результат пермножения элементов из файла и массива')
for i in range (0, n):
    print (int(index_array[i])*new_rand_array[i], end = ' ')
input()