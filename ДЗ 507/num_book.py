from tkinter import*
from model import*

def funcexp_csv():
    global table_meaning
    global list_meaning
    table_meaning = export_csv()
    list_meaning = Variable(value=table_meaning) 
    list_box.config(listvariable = list_meaning)

def funcimp_csv():
    global table_meaning
    impotr_csv(table_meaning)

def funcimp_txt():
    global table_meaning
    import_txt(table_meaning)

def funcexp_txt():
    global table_meaning
    global list_meaning
    table_meaning = export_txt()
    list_meaning = Variable(value=table_meaning) 
    list_box.config(listvariable = list_meaning)

book = Tk()
book.title('Записная книжка номеров')
book.geometry('1300x380')

# Верхнее меню
export_menu = Menu(tearoff=0)
export_menu.add_command(label="TXT", command = funcexp_txt)
export_menu.add_command(label="CSV", command = funcexp_csv)

import_menu = Menu(tearoff=0)
import_menu.add_command(label="TXT", command = funcimp_txt)
import_menu.add_command(label="CSV", command = funcimp_csv)

file_menu = Menu(tearoff=0) 
file_menu.add_cascade(label="Экспорт из ...", menu = export_menu)
file_menu.add_separator()
file_menu.add_cascade(label="Импорт в ...", menu = import_menu)
file_menu.add_separator()
file_menu.add_command(label="Выход", command = book.destroy)

file = Menu()
file.add_cascade(label="Файл", menu = file_menu)

book.config(menu=file)

table_meaning = {}
list_meaning = Variable(value=table_meaning)

# Интерфейс
input_frame = Frame()
title_place = Label (input_frame, text = '# Отключено' , font = "Arial 26", padx = 10, pady = 10)
title_place.grid(column = 0, row = 0, columnspan = 2)

name_label = Label (input_frame, text = 'Имя: ' , font = "Arial 20", padx = 10, pady = 10)
name_label.grid(column = 0, row = 1, sticky = 'e')
sename_label = Label (input_frame, text = 'Фамилия: ' , font = "Arial 20", padx = 10, pady = 10)
sename_label.grid(column = 0, row = 2, sticky = 'e')
number_label = Label (input_frame, text = 'Номер тел.: ' , font = "Arial 20", padx = 10, pady = 10)
number_label.grid(column = 0, row = 3, sticky = 'e')
about_label = Label (input_frame, text = 'Описание: ' , font = "Arial 20", padx = 10, pady = 10)
about_label.grid(column = 0, row = 4, sticky = 'e')

name_entry = Entry(input_frame, font =("Arial Bold", 20), width = 10)
name_entry.grid(column = 1, row = 1, sticky = 'w')
sename_entry = Entry(input_frame, font =("Arial Bold", 20), width = 20)
sename_entry.grid(column = 1, row = 2, sticky = 'w')
number_entry = Entry(input_frame, font =("Arial Bold", 20), width = 13, show = '*')
number_entry.grid(column = 1, row = 3, sticky = 'w')
about_text = Entry(input_frame, font =("Arial Bold", 20), width = 15)
about_text.grid(column = 1, row = 4, sticky = 'w')

input_btn = Button(input_frame, text = 'Добавить контакт' , font = "Arial 20", )
input_btn.grid(column = 0, row = 6, columnspan = 2, pady = 10)

input_frame.pack(side = 'left')

list_frame = Frame(padx = 10)
list_frame.pack(side = 'left')
list_box = Listbox(list_frame, listvariable = list_meaning, height = 10, width = 60, font = "Arial 20")
list_box.pack()

book.mainloop()