# -- coding: utf-8 --

def convert(n):
    s = ''
    while n > 0:
        s += str(n%2)
        n = n//2
    res = ''
    for i in range(len(s)):
        res += s[-i-1]
    return res

num = int(input('Введите число:'))
print(f'Число {num} в двоичной сис-ме = ', convert(num))
input()