ip = input().split('.')

count = 0

for i in ip:
    if 0 <= int(i) <= 255:
        count += 1

if count == 4:
    print('ДА')
else:
    print('НЕТ')