num = list()
flag = False

for i in range(int(input())):
    num.append(int(input()))
x = int(input())

for i in range(len(num)):
    for n in range(i+1, len(num)):
        if num[i] * num[n] == x:
            flag = True
            break

if flag == True:
    print('ДА')
else:
    print('НЕТ')