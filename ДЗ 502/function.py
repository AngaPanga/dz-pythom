# -- coding: utf-8 --

function_calculator = lambda n: (1+1/n)**n

# Код программы
n = int(input('Введите число N: '))
result_array = []
for i in range (1, n+1):
    result_array.append(function_calculator(i))
print(*result_array)
input()