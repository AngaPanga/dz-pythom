from math import*

# Определение четверти
def find_quarter():
    input_out = False
    print('Введите кординаты точки.')
    while input_out == False:
        print('Введите x = ', end = ' ')
        x = int(input())
        print('Введите y = ', end = ' ')
        y = int(input())
        if x == 0:
            print('Введено не корректное значение x. Повторите попытку')
        elif y == 0:
            print('Введено не корректное значение y. Повторите попытку')
        else:
            input_out = True
    if x > 0 and y > 0:
        print('Точка находится в 1 четверти.')
    elif x < 0 and y > 0:
        print('Точка находится в 2 четверти.')
    elif x > 0 and y < 0:
        print('Точка находится в 4 четверти.')
    else:
        print('Точка находится в 3 четверти.')
        
# Диапозоны четвертей
def quarter_info():
    print('Введите номер четверти - 1, 2, 3, 4')
    print('Ввод:', end = ' ')
    num_quarter = int (input())
    if num_quarter == 1:
        print('x принимает значения от 0 до ∞. y принимает значения от 0 до ∞.')
    elif num_quarter == 2:
        print('x принимает значения от 0 до -∞. y принимает значения от 0 до ∞.')
    elif num_quarter == 3:
        print('x принимает значения от 0 до -∞. y принимает значения от 0 до -∞.')
    elif num_quarter == 4:
        print('x принимает значения от 0 до ∞. y принимает значения от 0 до -∞.')
    else:
        print('Такой четверти нет.')

# Длина вектора
def vector_lenght():
    print('Введите кординаты точек')
    print('Введите x1 = ', end = ' ')
    x1 = int(input())
    print('Введите x2 = ', end = ' ')
    x2 = int(input())
    print('Введите y1 = ', end = ' ')
    y1 = int(input())
    print('Введите y2 = ', end = ' ')
    y2 = int(input())
    result = sqrt((x2-x1)**2+(y2-y1)**2)
    print(f'Длина вектора = {result.real}' )

# Код программы
out = False
while out == False:
    print('Выберете задачу, которую хотите выполнить')
    print('1. Определить четверть кординатной плоскости')
    print('2. Вывести диапозон четверти')
    print('3. Опредилить длину вектора')
    print('4. Выход')
    print('Введите номер задачи:', end = ' ')
    num_command = input()
    if num_command == '1':
        find_quarter()
        print()
    elif num_command == '2':
        quarter_info()
        print()
    elif num_command == '3':
        vector_lenght()
        print()
    elif num_command == '4':
        out = True
    else:
        print('Ввод неверен. Повторите попытку:', end = ' ')
        num_command = input()