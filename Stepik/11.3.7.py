n = int(input())

answer = list()
for el in range(n):
    word = input()
    answer.append(word)

k = int(input())

for i in range(n):
    if k <= len(answer[i]):
        print(answer[i][k-1], end = '')



