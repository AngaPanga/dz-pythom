# -- coding: utf-8 --

def negativ(array):
    arr = []
    arr.extend(array)
    del arr[0]
    for i in range (0, len(arr)):
        if i%2 == 1:
            arr[i] *=-1
    arr.reverse()
    return arr

def fibinachi(n):
    array = [0, 1]
    for i in range (2, n+1):
        array.append(array[i-1]+array[i-2])
    result = (negativ(array)) + array
    print('Ряд негафибаначи + фибаначи.\n',*result)


# Код программы
n = int(input('Введите N целое, где N устанавливает границы от -N до N\nN = '))
if n < 0:
    n *=-1

if n < 1:
    print('Ряд негафибаначи + фибаначи.\n0')
elif n < 2:
    print('Ряд негафибаначи + фибаначи.\n1 0 1')
else:
    fibinachi(n)
input()