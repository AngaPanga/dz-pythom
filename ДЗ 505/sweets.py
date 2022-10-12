# -- coding: utf-8 --
from tkinter import*
from random import*
import time

def ii_config(k):
    new_game()
    entry_2.grid_forget()
    btn2.grid_forget()
    level.set(k)

def light_ii():
    ii_config(1)

def hard_ii():
    ii_config(2)

def unstoppable_ii():
    ii_config(3)

def victory_check():
    if balance.get() == 0:
        stop_game.set(True)
        if turn.get() == True:
            balance_place.config(text = 'Победил игрок 1', font = 'Arial 22')
        else:
            balance_place.config(text = 'Победил игрок 2', font = 'Arial 22')

def replace_history(d):
    history_3.config(text = (history_2.cget('text')))
    history_2.config(text = (history_1.cget('text')))
    history_1.config(text = d)
    victory_check()

def do_p1():
    balance.set(balance.get() - int(entry_1.get()))
    balance_place.config(text = balance.get())
    player_1.set(player_1.get() + int(entry_1.get()))
    count_1.config(text = player_1.get())
    replace_history(('-' + (entry_1.get())))
    entry_1.delete(0, END)
    turn.set(False)
    name_1.config(bg = '#E9967A')
    name_2.config(bg = '#7CFC00')

def do_ii():
    time.sleep(1)
    temp = randrange(1, 16)
    balance.set(balance.get() - temp)
    balance_place.config(text = balance.get())
    player_2.set(player_2.get() + temp)
    count_2.config(text = player_2.get())
    replace_history(-(temp))
    entry_2.delete(0, END)
    turn.set(True)
    name_2.config(bg = '#E9967A')
    name_1.config(bg = '#7CFC00')

def do_ii2():
    time.sleep(1)
    temp = balance.get() % 16
    if temp == 0:
        temp = randrange(1, 16)
    balance.set(balance.get() - temp)
    balance_place.config(text = balance.get())
    player_2.set(player_2.get() + temp)
    count_2.config(text = player_2.get())
    replace_history(-(temp))
    entry_2.delete(0, END)
    turn.set(True)
    name_2.config(bg = '#E9967A')
    name_1.config(bg = '#7CFC00')

def do_ii3():
    if balance.get() > 37:
        temp = randrange(-10, 26)
    else:
        temp = balance.get() % 16
        if temp == 0:
            temp = 0 
    balance.set(balance.get() - temp)
    balance_place.config(text = balance.get())
    player_2.set(player_2.get() + temp)
    count_2.config(text = player_2.get())
    replace_history(-(temp))
    entry_2.delete(0, END)
    turn.set(True)
    name_2.config(bg = '#E9967A')
    name_1.config(bg = '#7CFC00')

def btn1_check():
    if level.get() == 0:
        if 16 > int(entry_1.get()) > 0 and balance.get() >= int(entry_1.get()) and turn.get() == True:
            do_p1()
    elif level.get() == 1:
        if 16 > int(entry_1.get()) > 0 and balance.get() >= int(entry_1.get()) and turn.get() == True:
            do_p1()
            if stop_game.get()== False:
                do_ii()
    elif level.get() == 2:
        if 16 > int(entry_1.get()) > 0 and balance.get() >= int(entry_1.get()) and turn.get() == True:
            do_p1()
            if stop_game.get()== False:
                do_ii2()
    elif level.get() == 3:
        if 16 > int(entry_1.get()) > 0 and balance.get() >= int(entry_1.get()) and turn.get() == True:
            do_p1()
            if stop_game.get()== False:
                do_ii3()

        
def btn2_check():
    if 16 > int(entry_2.get()) > 0 and balance.get() >= int(entry_2.get()) and turn.get() == False:
        balance.set(balance.get() - int(entry_2.get()))
        balance_place.config(text = balance.get())
        player_2.set(player_2.get() + int(entry_2.get()))
        count_2.config(text = player_2.get())
        replace_history(('-' + (entry_2.get())))
        entry_2.delete(0, END)
        turn.set(True)
        name_2.config(bg = '#E9967A')
        name_1.config(bg = '#7CFC00')

def new_game():
    stop_game.set(False)
    balance.set(100)
    player_1.set(0)
    player_2.set(0)
    turn.set(True)
    balance_place.config(text = balance.get() , font = "Arial 36")
    count_1.config(text = player_1.get())
    count_2.config(text = player_2.get())
    history_1.config(text = '')
    history_2.config(text = '')
    history_3.config(text = '')
    name_1.config (bg = '#7CFC00')
    name_2.config (bg = '#E9967A')

# Код программы
game = Tk()
game.title("Конфетки")
game.geometry("450x400")

game_menu = Menu(tearoff=0) 
game_menu.add_command(label="New PvP", command = new_game)
game_menu.add_separator()
game_menu.add_command(label="New light ii", command = light_ii)
game_menu.add_command(label="New Hard ii", command = hard_ii)
game_menu.add_separator()
game_menu.add_command(label="Loser ii", command = unstoppable_ii)
game_menu.add_separator()
game_menu.add_command(label="Exit", command=game.destroy)

bar_menu = Menu()
bar_menu.add_cascade(label="Игра", menu = game_menu) # Прикрепить меню игры к первой позиции.

game.config(menu=bar_menu)

instruction_game = Label (text= '''Игра отними конфетки!\n
Каждый игрок ходит по очереди и берет любое число конфет\n
от 1 до 15. Побеждает тот кто возьмет последние конфеты!\n
Первым ходит Игрок 1 с зеленым индекатором. В меню "Игра"\n
можно запустить игру заново, пункт "New PvP".''', font = "Arial 11", padx = 10, pady = 1)
instruction_game.grid(column = 0, row = 0, columnspan = 5)

stop_game = BooleanVar()
stop_game.set(False)
turn = BooleanVar()
turn.set(True)
balance = IntVar()
balance.set(100)
player_1 = IntVar()
player_1.set(0)
player_2 = IntVar()
player_2.set(0)
level = IntVar()
level.set(0)

balance_place = Label (text = balance.get() , font = "Arial 36", padx = 10, pady = 10)
balance_place.grid(column = 1, row = 1, columnspan = 3)
count_1 = Label (text = player_1.get() , font = "Arial 28", padx = 10, pady = 10)
count_1.grid(column = 0, row = 4, columnspan = 2)
count_2 = Label (text = player_2.get() , font = "Arial 28", padx = 10, pady = 10)
count_2.grid(column = 3, row = 4, columnspan = 2)
history_1 = Label (font = "Arial 28", padx = 10, pady = 3, width = 3)
history_1.grid(column = 2, row = 2)
history_2 = Label (font = "Arial 28", padx = 10, pady = 3, width = 3)
history_2.grid(column = 2, row = 3)
history_3 = Label (font = "Arial 28", padx = 10, pady = 3, width = 3)
history_3.grid(column = 2, row = 4)

name_1 = Label (text = "Игрок 1" , font = "Arial 24", bg = '#7CFC00', padx = 10, pady = 10)
name_1.grid(column = 0, row = 2, columnspan = 2)
name_2 = Label (text = "Игрок 2" , font = "Arial 24", bg = '#E9967A', padx = 10, pady = 10)
name_2.grid(column = 3, row = 2, columnspan = 2)

entry_1 = Entry(font =("Arial Bold", 28), width = 3)
entry_1.grid(column = 1, row = 3)
entry_2 = Entry(font =("Arial Bold", 28), width = 3)
entry_2.grid(column = 3, row = 3)

btn1 = Button(text = 'Забрать', command = btn1_check, padx = 3, pady = 3)
btn1.grid(column = 0, row = 3)
btn2 = Button(text = 'Забрать', command = btn2_check, padx = 3, pady = 3)
btn2.grid(column = 4, row = 3)

game.mainloop()