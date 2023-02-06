n = input()

digit ='0123456789'
count = 0
for i in range(len(n)):
    if n[i] in digit:
        count+=1

if count > 0:
    print('Цифра')
else:
    print('Цифр нет')