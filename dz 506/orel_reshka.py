# -- coding: utf-8 --

data = 'ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООО'
print(data)
code = []
prev_char = ''
count = 1 

for ch_one in data: 
    if ch_one != prev_char:
        if prev_char == 'Р': 
            code.append(count)
        count = 1
        prev_char = ch_one 
    else: 
        count += 1 
else:
    if prev_char == 'Р':
       code.append(count)

print(max(code))