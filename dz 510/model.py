from random import randint


def play(data):
    if data.isnumeric():
        num = int(data)
        return examination(num)
    else:
        return 'Введены не корректные данные'


def examination(num):
    if 0 < num < 16:
        return calculate(num)
    else:
        return 'Введено не допустимое значение конфет!\nПовторите попытку'


def calculate(amount):
    global balance
    balance -= amount
    if balance < 1:
        global status
        status = True
        return 'Ты победил! Поздравляю!'
    else:
        text = f'Конфет осталось {balance}\n' + bot_action()
        return text


def bot_action():
    global balance
    box = balance % 16
    if box == 0:
        box = randint(1,15)
    balance -= box
    if balance < 1:
        global status
        status = True
        return 'Победил Бот! Старайся лучше!'
    else:
        history = f'Бот взял {box}\nКонфет осталось {balance}\n Твой ход'
        return history


def change_balance(inp_balance):
    global balance
    balance = int(inp_balance)


def info_play():
    return 'На столе лежат конфеты.\nКаждый игрок может взять от 1 до 15 конфет.\nВыигрывает тот, кто возьмет конфеты последним.'


balance = 100
status = False