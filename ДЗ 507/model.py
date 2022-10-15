import csv

def export_csv():
    data = []
    with open("book.csv", "r", encoding = 'utf-8', newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(';'.join(row))
    return data


def impotr_csv(data):
    data = list(el.split(';') for el in data)
    with open("book_imp.csv", "w", encoding = 'utf-8', newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

def export_txt():
    with open('book.txt', 'r', encoding = 'utf-8') as file:
        exp_data = file.read()
        data = exp_data.split('\n')
    return data

def import_txt(data):
    with open('book_imp.txt', 'w', encoding = 'utf-8') as file:
        for el in data:
            file.write(el + '\n')