# -- coding: utf-8 --
from math import gcd

num = 36
array = [12,144,18]
for i in array:
    num = gcd(num, i)
print ('Наибольший результирующий общий делитель = ', num)