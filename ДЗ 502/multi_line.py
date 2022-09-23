# -- coding: utf-8 --

n = int(input('Введите число N: ')) + 1
result = 1
for i in range (1, n):
    result *= i
    print(result, end = ' ')
input()