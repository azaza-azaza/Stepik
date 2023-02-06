l = input().split()
m = input().split()
answer = list()

for i in range(len(l)):
    a = int(l[i]) + int(m[i])
    answer.append(a)

print(*answer, sep = ' ')
