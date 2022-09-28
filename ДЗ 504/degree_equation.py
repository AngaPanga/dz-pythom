# -- coding: utf-8 --
from random import*

# Массив случайных коэфицентов
def random_array(n):
    arr = []
    for i in range (n):
        arr.append(randrange(-100, 100))
    print(*arr)
    return arr

def create_degree(k):
    array = random_array(k+1)
    degree = ''
    for i in array:
        if i != 0 and i > 0:
            degree += positive_line(k, i)
        elif i != 0 and i < 0: 
            degree += negative_line(k, i)
        k -= 1
    wrt_file(degree)


def positive_line(k, i):
    if k != 0 and k != 1 and i != 1:
        s = (f'+ {i}*x^{k} ')
    elif k != 0 and k == 1 and i != 1:
        s = (f'+ {i}*x ')
    elif k != 0 and k != 1 and i == 1:
        s = (f'+ x^{k} ')
    elif k != 0 and k == 1 and i == 1:
        s = (f'+ x ')
    elif k == 0 and i == 0:
        s = ('= 0')
    else:
        s = (f'+ {i} = 0')
    return s

def negative_line(k, i):
    if k != 0 and k != 1 and abs(i) != 1:
        s = (f'- {abs(i)}*x^{k} ')
    elif k != 0 and k != 1 and i == -1:
        s = (f'- x^{k} ')
    elif k != 0 and k == 1 and i != -1:
        s = (f'- {abs(i)}*x ')
    elif k != 0 and k == 1 and i == -1:
        s = (f'- x ')
    elif k == 0 and i == 0:
        s = ('= 0')
    else:
        s= (f'- {abs(i)} = 0')
    return s

def wrt_file(deg):
    if deg[0] == '+':
        deg = deg.replace('+', '', 1)
    with open ('res_degree.txt', 'w') as file:
        file.write(deg)
    file.close()


# Код программы
number = int (input('Введите степень уровнения: '))
create_degree(number)
input()
