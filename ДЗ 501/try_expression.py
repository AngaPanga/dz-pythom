print('Проверим на истиность выражение: ¬(X V Y V Z) = ¬X ^ ¬Y ^ ¬Z\n')
count = 15
out = False
while out == False:
    box = str(bin(count))
    if len(box)>3:
        x = int(box[3])
    if len(box)>4:
        y = int(box[4])
    if len(box)>5:
        z = int(box[5])
    print(f'Подставим следущие значения: x = {x}, y = {y}, z = {z}')
    res1 = not(x and y and z)
    res2 = (not x) or (not y) or (not z)
    if res1 == res2:
        print(f'Результат вычисления: {res1} = {res2} - Верно \n')
    count -=1
    if count < 8:
        out = True
input()    