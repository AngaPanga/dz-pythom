# -- Coding: utf-8 -- 

# Поиск множителей
def find_multipliers(num):
    n = num
    i = 2
    array = []
    while n != 1:
        if n % i == 0:
            array.append(i)
            n /= i 
        else:
           i += 1    
    print(f'Простые множетели числа {num}:', *array)

# Код программы
number = int (input('Введите число: '))
find_multipliers(number)
input()