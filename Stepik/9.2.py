n = input()
count = 0
for i in range(0, len(n)//2):
    if n[i] != n[-i-1]:
        print('NO')
        count+=1
        break
if count == 0:
    print('YES')