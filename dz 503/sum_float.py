# -- coding: utf-8 --

# Отсечение целой части
def convert_elements(arr):
    for i in range (0, len(arr)):
        box = str(arr[i])
        tmp_i = box.find('.')
        box ='0' + box[tmp_i:]
        arr[i] = float(box)
    return arr

# Разница максимального и мининального
def diferent_max_min(arr):
    arr = convert_elements(arr)
    print('Разница между дробной максимальной и минимальной частями числа = ', max(arr) - min(arr))

# Код программы
array = [0.5, 15.158, 5.79615, 8798.4, -486.3871]
print(*array)
diferent_max_min(array)
input()