n = int(input())

answer = list()
for i in range(n):
    digit = int(input())
    answer.append(digit)

del answer[1::2]
print(answer)