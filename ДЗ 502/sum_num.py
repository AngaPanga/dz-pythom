# -- coding: utf-8 --

# Вырезание точки из числа
def replace_num(a):
    s = str(a)
    s = s.replace('.','')
    return int(s)

# Подсчет суммы цифр
def sum_num(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num = num//10
    return sum

# Код программы
float_num = float(input('Введите любое число:'))
result = replace_num(float_num)
result = sum_num(result)
print (f'Сумма цифр в числе {float_num} = {result}')
input()