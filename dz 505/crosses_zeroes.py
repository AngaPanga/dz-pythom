# -- coding: utf-8 --
from tkinter import *

def new_game():
    forget_old()
    nadpis.pack()
    krestik.pack()
    nadpis.config(text= "Ходит игрок 1")
    btn1.grid(column=0, row=0)
    btn2.grid(column=1, row=0)
    btn3.grid(column=2, row=0)
    btn4.grid(column=0, row=1)
    btn5.grid(column=1, row=1)
    btn6.grid(column=2, row=1)
    btn7.grid(column=0, row=2)
    btn8.grid(column=1, row=2)
    btn9.grid(column=2, row=2)
    player.set(1)
    global array
    array = [2,2,2,2,2,2,2,2,2]

def forget_old():
    pm.pack_forget()
    place1.grid_forget()
    place2.grid_forget()
    place3.grid_forget()
    place4.grid_forget()
    place5.grid_forget()
    place6.grid_forget()
    place7.grid_forget()
    place8.grid_forget()
    place9.grid_forget()

def pl1_o(f):
    if f == 1:
        place1.config(image = img2)
        place1.grid(column=0, row=0)
    else:
        place1.config(image = img3)
        place1.grid(column=0, row=0)

def pl2_o(f):
    if f == 1:
        place2.config(image = img2)
        place2.grid(column=1, row=0)
    else:
        place2.config(image = img3)
        place2.grid(column=1, row=0)

def pl3_o(f):
    if f == 1:
        place3.config(image = img2)
        place3.grid(column=2, row=0)
    else:
        place3.config(image = img3)
        place3.grid(column=2, row=0)

def pl4_o(f):
    if f == 1:
        place4.config(image = img2)
        place4.grid(column=0, row=1)
    else:
        place4.config(image = img3)
        place4.grid(column=0, row=1)

def pl5_o(f):
    if f == 1:
        place5.config(image = img2)
        place5.grid(column=1, row=1)
    else:
        place5.config(image = img3)
        place5.grid(column=1, row=1)

def pl6_o(f):
    if f == 1:
        place6.config(image = img2)
        place6.grid(column=2, row=1)
    else:
        place6.config(image = img3)
        place6.grid(column=2, row=1)

def pl7_o(f):
    if f == 1:
        place7.config(image = img2)
        place7.grid(column=0, row=2)
    else:
        place7.config(image = img3)
        place7.grid(column=0, row=2)

def pl8_o(f):
    if f == 1:
        place8.config(image = img2)
        place8.grid(column=1, row=2)
    else:
        place8.config(image = img3)
        place8.grid(column=1, row=2)

def pl9_o(f):
    if f == 1:
        place9.config(image = img2)
        place9.grid(column=2, row=2)
    else:
        place9.config(image = img3)
        place9.grid(column=2, row=2)
    
def end_game():
    krestik.pack_forget()
    if player.get() == 1: 
        nadpis.pack_forget()
        pm.config(text ="Победил игрок 1", padx = 10, pady = 10)
        pm.pack()   
    elif player.get() == 0:
        nadpis.pack_forget()
        pm.config( text ="Победил игрок 2", font = "Arial 28", padx = 10, pady = 10)
        pm.pack()
    else:
        nadpis.pack_forget()
        pm.config( text ="Ничья", font = "Arial 28", padx = 10, pady = 10)
        pm.pack()
    
def p1():
    array[0] = player.get()
    if player.get() == 1:
        pl1_o(1)
        check()
        k = player.get() + 1
        player.set(0)
    else:
        pl1_o(0)
        check()
        k = player.get() + 1
        player.set(1)
    nadpis.config(text= f"Ходит игрок {k}")
    btn1.grid_forget()

def p2():
    array[1] = player.get()
    if player.get() == 1:
        pl2_o(1)
        check()
        k = player.get() + 1
        player.set(0)
    else:
        pl2_o(0) 
        check()
        k = player.get() + 1
        player.set(1)
    nadpis.config(text= f"Ходит игрок {k}")
    btn2.grid_forget()

def p3():
    array[2] = player.get()
    if player.get() == 1:
        pl3_o(1)
        check()
        k = player.get() + 1
        player.set(0)
    else:
        pl3_o(0)
        check()
        k = player.get() + 1
        player.set(1)
    nadpis.config(text= f"Ходит игрок {k}")
    btn3.grid_forget()

def p4():
    array[3] = player.get()
    if player.get() == 1:
        pl4_o(1)
        check()
        k = player.get() + 1
        player.set(0)
    else:
        pl4_o(0)
        k = player.get() + 1
        player.set(1)
    nadpis.config(text= f"Ходит игрок {k}")
    btn4.grid_forget()

def p5():
    array[4] = player.get()
    if player.get() == 1:
        pl5_o(1)
        check()
        k = player.get() + 1
        player.set(0)
    else:
        pl5_o(0)
        check()
        k = player.get() + 1
        player.set(1)
    nadpis.config(text= f"Ходит игрок {k}")
    btn5.grid_forget()

def p6():
    array[5] = player.get()
    if player.get() == 1:
        pl6_o(1)
        check()
        k = player.get() + 1
        player.set(0)
    else:
        pl6_o(0)
        check()
        k = player.get() + 1
        player.set(1)
    nadpis.config(text= f"Ходит игрок {k}")
    btn6.grid_forget()

def p7():
    array[6] = player.get()
    if player.get() == 1:
        pl7_o(1)
        check()
        k = player.get() + 1
        player.set(0)
    else:
        pl7_o(0)
        check()
        k = player.get() + 1
        player.set(1)
    nadpis.config(text= f"Ходит игрок {k}")
    btn7.grid_forget()

def p8():
    array[7] = player.get()
    if player.get() == 1:
        pl8_o(1)
        check()
        k = player.get() + 1
        player.set(0)
    else:
        pl8_o(0)
        check()
        k = player.get() + 1
        player.set(1)
    nadpis.config(text= f"Ходит игрок {k}")
    btn8.grid_forget()

def p9():
    array[8] = player.get()
    if player.get() == 1:
        pl9_o(1)
        check()
        k = player.get() + 1
        player.set(0)
    else:
        pl9_o(0)
        check()
        k = player.get() + 1
        player.set(1)
    nadpis.config(text= f"Ходит игрок {k}")
    btn9.grid_forget()

def check():
    a1 = (array[0] == array[1] == array[2] == player.get())
    a2 = (array[0] == array[3] == array[6] == player.get())
    a3 = (array[0] == array[4] == array[8] == player.get())
    a4 = (array[1] == array[4] == array[7] == player.get())
    a5 = (array[2] == array[5] == array[8] == player.get())
    a6 = (array[2] == array[4] == array[6] == player.get())
    a7 = (array[3] == array[4] == array[5] == player.get())
    a8 = (array[6] == array[7] == array[8] == player.get())
    if a1 or a2 or a3 or a4 or a5 or a6 or a7 or a8:
        end_game()
    elif array.count(2) == 0:
        player.set(2)
        end_game()

# Код программы
game = Tk()
game.title("Крестики нолики вдвоем")
game.geometry("330x380")

game_menu = Menu(tearoff=0)
game_menu.add_command(label="Новая", command = new_game )
game_menu.add_separator()
game_menu.add_command(label="Выход", command=game.destroy)

bar_menu = Menu()
bar_menu.add_cascade(label="Игра", menu = game_menu) # Прикрепить меню игры к первой позиции.

game.config(menu=bar_menu)

nadpis = Label (text= "Ходит игрок 1", font = "Arial 28", padx = 10, pady = 10)
pm = Label (text= " ", font = "Arial 28", padx = 10, pady = 10)
krestik = Frame(game)

player = IntVar()
array = [2,2,2, 2,2,2, 2,2,2]
img = PhotoImage(file = 'joystick.png')
img2 = PhotoImage(file = 'cross.png')
img3 = PhotoImage(file = 'zero.png')
    
btn1 = Button(krestik, image = img, command = p1, padx = 3, pady = 3)
btn2 = Button(krestik, image = img, command = p2, padx = 3, pady = 3)
btn3 = Button(krestik, image = img, command = p3, padx = 3, pady = 3)
btn4 = Button(krestik, image = img, command = p4, padx = 3, pady = 3)
btn5 = Button(krestik, image = img, command = p5, padx = 3, pady = 3)
btn6 = Button(krestik, image = img, command = p6, padx = 3, pady = 3)
btn7 = Button(krestik, image = img, command = p7, padx = 3, pady = 3)
btn8 = Button(krestik, image = img, command = p8, padx = 3, pady = 3)
btn9 = Button(krestik, image = img, command = p9, padx = 3, pady = 3)

place1 = Label (krestik, image = img2)
place2 = Label (krestik, image = img2)
place3 = Label (krestik, image = img2)
place4 = Label (krestik, image = img2)
place5 = Label (krestik, image = img2)
place6 = Label (krestik, image = img2)
place7 = Label (krestik, image = img2)
place8 = Label (krestik, image = img2)
place9 = Label (krestik, image = img2)

game.mainloop()