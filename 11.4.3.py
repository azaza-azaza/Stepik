n = int(input())
answer = list()

for el in range(n):
    word = input()
    if word not in answer:
        answer.append(word)

print(*answer, sep = '\n')