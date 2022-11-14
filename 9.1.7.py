n = input()

a = 'а, у, о, ы, и, э, я, ю, ё, е'
b = 'б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ'

count_a = 0
count_b = 0

for i in range(len(n)):
    if n[i] == '+':
        count_pl += 1
    elif n[i] == '*':
        count_zv += 1

print('Количество гласных букв равно', count_a)
print('Количество согласных букв равно', count_b)
