n = int(input())

i = 0
ii = 0
iii = 0
iv = 0

for j in range(n):
    x = [int(k) for k in input().split()]
    # if x[0] == 0 or x[1] == 0:
    #     continue
    if x[0] > 0:
        if x[1] > 0:
            i += 1
        elif x[1] < 0:
            iv += 1
    elif x[0] < 0:
        if x[1] > 0:
            ii += 1
        elif x[1] < 0:
            iii += 1

print('Первая четверть:', i)
print('Вторая четверть:', ii)
print('Третья четверть:', iii)
print('Четвертая четверть:', iv)
