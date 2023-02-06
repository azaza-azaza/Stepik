n = int(input())

list_of_n = list()
for i in range(n):
    digit = int(input())
    list_of_n.append(digit)

answer = list()
for k in range(len(list_of_n)-1):
    x = list_of_n[k] + list_of_n[k+1]
    answer.append(x)
print(answer)