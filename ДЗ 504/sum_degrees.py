# -- coding: utf-8 --
# 25*x^2 - 61*x + 77 = 0

convert_line = lambda s: s.replace(' ', '').replace('*', '').replace('+', ' ').replace('-', ' -').replace('=0', '').replace('-x', '-1x').replace(' x', '1x').lstrip()

def read_file(name_file):
    with open (name_file, 'r') as file:
        line = file.readline()
    file.close()
    arr = convert_line(line).split(' ')
    return arr

def array_to_dict(array):
    d = {}
    for i in array:
        if i.find('^')>-1:
            d[int(i[i.find('^')+1:])] = int(i[:i.find('x')])
        elif i.find('x')>-1:
            d[1] = int(i[:i.find('x')])
        else:
            d[0] = int(i)
    return d

def result_dict(ar1, ar2):
    d1 = array_to_dict(ar1)
    d2 = array_to_dict(ar2)
    for key in d1:
        d1[key] += d2.get(key, 0)
        if key in d2:
            del d2[key]
    d1.update(d2)
    d1 = dict(reversed(sorted(d1.items(), key = lambda x: x[0])))
    for key in d1:
        if d1[key] > 0:
            d1[key] ='+ ' + str(d1[key])
        elif d1[key] < 0:
            d1[key] =str(d1[key])
        temp = []
        for key in d1:
            if d1[key] == 0:
                temp.append(key)
    for i in temp:
        if d1[i] == 0:
            del d1[i]
    return d1

def result_degree():
    res = ''
    name_one = 'degree_one.txt'
    name_teo = 'degree_two.txt'
    array_1 = read_file(name_one)
    array_2 = read_file(name_teo)
    res_dict = result_dict(array_1, array_2)
    print(res_dict)
    for key in res_dict:
        if key > 1:
            res +=' ' + res_dict[key] + 'x^'+ str(key)
        elif key ==1:
            res +=' ' + res_dict[key] + 'x'
        else:
            res +=' ' + res_dict[key]
    res = convert_result(res)
    with open ('res_sum_degree', 'w') as file:
        file.write(res)
    file.close()

def convert_result(s):
    if s[1] == '+':
        del s[1]
    s = s.replace('-', '- ').lstrip()
    return s

# Код программы
result_degree()
input()