# -- Coding: utf-8 --

# Функция преобразования числа к заданной точности
def given_accuracy(num, d):
    num = num*(10**(d+1))
    num = int(num)
    ost = num % 10
    num //= 10
    if ost > 4:
        num += 1
    num = (float(num))/(10**d)
    return num

# Код программы
number = float(input('Введите число: '))
count_signs = int (input('Введите точность: '))
print(given_accuracy(number, count_signs))
input()