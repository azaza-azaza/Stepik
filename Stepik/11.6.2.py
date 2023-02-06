text = input().split()

articles = ['a', 'an', 'the']
count = 0
for el in articles:
    for i in text:
        if el == i.lower():
            count += 1

print('Общее количество артиклей:', count)

