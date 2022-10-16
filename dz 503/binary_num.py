# -- coding: utf-8 --

# Преобразование числа
def convert_num(n):
    s = str(bin(n))
    s = s[2:]
    print('Данное число в двоичном коде =', s)

# Код программы
num = int(input('Введите число для преобразования: '))
convert_num(num)
input()