from tkinter import*
from tkinter import messagebox
from model import*

def information():
    messagebox.showinfo('Справка по программе',
    '''        В меню "Файл" можно экспортировать/импортировать
    файлы справочника. Экспортировать можно несколько
    раз, как следствие файлы объеденяются в один спиок.
        С помощью кнопки "Добавить" можно добать новый
    контакт в конец справочника.
        С помощью кнопки "Удалить" можно удалить 
    выбранный контакт из списка.
        С помощью кнопки "<--" можно выбрать контакт
    для изменения, а затем сохранить кнопкой "Изменить".''')

def del_element():
    list_box.delete(list_box.curselection())

def input_element():
    box = (name_entry.get() + '; ' + 
    sename_entry.get() + '; ' + 
    second_name_entry.get() + '; ' + 
    number_entry.get() + '; ' + 
    about_entry.get())
    name_entry.delete(0, END)
    sename_entry.delete(0, END)
    second_name_entry.delete(0, END)
    number_entry.delete(0, END)
    about_entry.delete(0, END)
    list_box.insert(END, box)

def convert_entrys():
    global index
    index = list_box.curselection()
    element = list_box.get(list_box.curselection()).split('; ')
    change_status.set(True)
    name_entry.delete(0, END)
    name_entry.insert(0, element[0])
    sename_entry.delete(0, END)
    sename_entry.insert(0, element[1])
    second_name_entry.delete(0, END)
    second_name_entry.insert(0, element[2])
    number_entry.delete(0, END)
    number_entry.insert(0, element[3])
    about_entry.delete(0, END)
    about_entry.insert(0, element[4])


def change_element():
    if change_status.get():
        global index
        list_box.delete(index)
        box = (name_entry.get() + '; ' + 
        sename_entry.get() + '; ' + 
        second_name_entry.get() + '; ' + 
        number_entry.get() + '; ' + 
        about_entry.get())
        name_entry.delete(0, END)
        sename_entry.delete(0, END)
        second_name_entry.delete(0, END)
        number_entry.delete(0, END)
        about_entry.delete(0, END)
        list_box.insert(index, box)
        change_status.set(False)

def funcexp_csv():
    global table_meaning
    global list_meaning
    table_meaning += export_csv()
    list_meaning = Variable(value=table_meaning) 
    list_box.config(listvariable = list_meaning)

def funcimp_csv():
    new_list = list(list_box.get(0, END))
    impotr_csv(new_list)

def funcimp_txt():
    new_list = list(list_box.get(0, END))
    import_txt(new_list)

def funcexp_txt():
    global table_meaning
    global list_meaning
    table_meaning += export_txt()
    list_meaning = Variable(value=table_meaning) 
    list_box.config(listvariable = list_meaning)

book = Tk()
book.title('Записная книжка номеров')
book.geometry('1300x400')

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
file.add_command(label="Справка", command = information)

book.config(menu=file)

change_status = BooleanVar()
change_status.set(False)
index = Variable()
table_meaning = []
list_meaning = Variable(value=table_meaning)

# Интерфейс
input_frame = Frame()
title_place = Label (input_frame, text = 'Телефонный справочник' , font = "Arial 26", padx = 10, pady = 10)
title_place.grid(column = 0, row = 0, columnspan = 3)

name_label = Label (input_frame, text = 'Имя: ' , font = "Arial 20", padx = 10, pady = 10)
name_label.grid(column = 0, row = 1, sticky = 'e')
sename_label = Label (input_frame, text = 'Фамилия: ' , font = "Arial 20", padx = 10, pady = 10)
sename_label.grid(column = 0, row = 2, sticky = 'e')
second_name_label = Label (input_frame, text = 'Отчество: ' , font = "Arial 20", padx = 10, pady = 10)
second_name_label.grid(column = 0, row = 3, sticky = 'e')
number_label = Label (input_frame, text = 'Номер тел.: ' , font = "Arial 20", padx = 10, pady = 10)
number_label.grid(column = 0, row = 4, sticky = 'e')
about_label = Label (input_frame, text = 'Описание: ' , font = "Arial 20", padx = 10, pady = 10)
about_label.grid(column = 0, row = 5, sticky = 'e')

name_entry = Entry(input_frame, font =("Arial Bold", 20), width = 10)
name_entry.grid(column = 1, row = 1, sticky = 'w')
sename_entry = Entry(input_frame, font =("Arial Bold", 20), width = 15)
sename_entry.grid(column = 1, row = 2, columnspan = 2, sticky = 'w')
second_name_entry = Entry(input_frame, font =("Arial Bold", 20), width = 15)
second_name_entry.grid(column = 1, row = 3, columnspan = 2, sticky = 'w')
number_entry = Entry(input_frame, font =("Arial Bold", 20), width = 15)
number_entry.grid(column = 1, row = 4, columnspan = 2, sticky = 'w')
about_entry = Entry(input_frame, font =("Arial Bold", 20), width = 15)
about_entry.grid(column = 1, row = 5, columnspan = 2, sticky = 'w')

input_btn = Button(input_frame, text = 'Добавить' , font = "Arial 18", command = input_element)
input_btn.grid(column = 0, row = 6, padx = 10, sticky = 'e')
change_btn = Button(input_frame, text = 'Изменить' , font = "Arial 18", command = change_element)
change_btn.grid(column = 1, row = 6, padx = 10)
del_btn = Button(input_frame, text = 'Удалить' , font = "Arial 18", command = del_element)
del_btn.grid(column = 2, row = 6, padx = 10)
rework_btn = Button(input_frame, text = '<--' , font = "Arial 18", command = convert_entrys)
rework_btn.grid(column = 2, row = 1, padx = 10)


input_frame.pack(side = 'left')

list_frame = Frame(padx = 10)
list_frame.pack(side = 'left')
list_box = Listbox(list_frame, listvariable = list_meaning, height = 10, width = 60, font = "Arial 20")
scrollbar = Scrollbar(list_frame, orient="vertical", command = list_box.yview)
list_box.config(yscrollcommand = scrollbar.set)
scrollbar.pack(side = RIGHT, fill = Y)
list_box.pack()

book.mainloop()