n = input().lower()

a = 'ауоыиэяюёе'
b = 'бвгджзйклмнпрстфхцчшщ'

count_a = 0
count_b = 0
# count_c = 0

for i in range(len(n)):
    if n[i] in a:
        count_a += 1
    elif n[i] in b:
        count_b += 1
    # else:
    #     count_c+=1

print('Количество гласных букв равно', count_a)
print('Количество согласных букв равно', count_b)
