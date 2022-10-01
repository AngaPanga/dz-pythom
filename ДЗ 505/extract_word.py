# -- coding: utf-8 --

def read_rus_file(name):
    with open (name, 'r', encoding = "utf-8") as file:
        line = file.read()
    file.close()
    arr = line.lower().split(' ')
    return arr

def ext_w(arr, err):
    txt = ''
    for i in range(len(arr)):
        if err in (arr[i]):            
            arr[i] = ''
    for i in arr:
        txt += i + ' '
    return txt

def write_file(name, txt):
    with open (name, 'w', encoding = "utf-8") as file:
        file.write(txt)
    file.close() 

# Код программы
name = 'text.txt'
array = read_rus_file(name)
error = input('Введите ошибку: ')
text = ext_w(array, error)
name = 'result.txt'
write_file(name, text)