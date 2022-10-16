# -- coding: utf-8 --

def read_file(name_file):
    with open (name_file, 'r') as file:
        line = file.read()
    file.close()
    if line:
        line = line.replace('\n', '')
        return line
    else:
        return ''


def write_file(name, code):
    if code:
        with open (name, 'w') as file:
            file.write(code)
        file.close()

def rle_code(data):
    code = ''
    prev_char = ''
    count = 1 
    if not data: return '' 
    for ch_one in data: 
        if ch_one != prev_char:
            if prev_char: 
                code += str(count) + prev_char 
            count = 1 
            prev_char = ch_one 
        else: 
            count += 1 
    else:
        code += str(count) + prev_char 
    return code

def rle_uncode(code):
    data =''
    count = ''
    for ch_one in code:
        if ch_one.isdigit():
            count += ch_one
        else:
            data += ch_one*int(count)
            count = ''
    return data
            
# Код программы
name = 'origin.txt'
text = read_file(name) # Считывание файл
text = rle_code(text) # Сжатие
name = 'code.txt'
write_file(name, text) # Запись в файл
if text:
    text = read_file(name) # Считывание файл
name = 'uncode.txt'
text = rle_uncode(text) # Разложение
write_file(name, text) # Запись в файл
input()