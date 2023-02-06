num = input().split('-')
number = True

# print(len(num))

if len(num) == 4:
    if num[0] != '7':
        number = False
elif len(num) == 3:
    if len(num[0]) == len(num[1]) == 3 and len(num[2]) == 4:
        number = True
    else:
        number = False
else:
    number = False
for i in num:
    if i.isdigit():
        continue
    else:
        number = False
        break

if number == True:
    print('YES')
else:
    print('NO')