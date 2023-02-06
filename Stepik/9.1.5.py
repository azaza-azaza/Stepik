n = input()

count_pl = 0
count_zv = 0

for i in range(len(n)):
    if n[i] == '+':
        count_pl += 1
    elif n[i] == '*':
        count_zv += 1

print('Символ + встречается', count_pl, 'раз')
print('Символ * встречается', count_zv, 'раз')