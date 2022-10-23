import csv

def index_get(i):
    global index
    global data
    index = i
    return data[i]

def import_csv():
    temp_data = list()
    with open("book.csv", "r", encoding='utf-8', newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            temp_data.append(';'.join(row))
    return temp_data


def save_data():
    global data
    convert_data = list(el.split(';') for el in data)
    with open("book.csv", "w", encoding='utf-8', newline="") as file:
        writer = csv.writer(file)
        writer.writerows(convert_data)


def print_data():
    global data
    text = ''
    for i, el in enumerate(data):
        text += str(i) + '. ' + el + '\n'
    return text


def delete_line(i):
    global data
    del data[i]
    text = print_data()
    return text


def add_line(line):
    global data
    data.append(line)
    text = print_data()
    return text


def change_line(line):
    global data
    global index
    data[index] = line
    text = print_data()
    return text


data = import_csv()
index = 0