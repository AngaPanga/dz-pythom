# -- coding: utf-8 --
from random import*

def random_array(original_arr):
    new_arr = []
    count = len(original_arr)
    for i in range (0, count):
        temp_index = randint(0, len(original_arr)-1)
        new_arr.append(original_arr[temp_index])
        del original_arr[temp_index]
    return new_arr

user_array = [1,2,3,4,5,6,7,8,9,10]
print('Стартовый массив \n', *user_array)
user_array = random_array(user_array)
print('Случайно отсортированный массив \n', *user_array)
input()