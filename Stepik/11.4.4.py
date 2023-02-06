n = int(input())
answer = list()

for el in range(n):
    word = input()
    answer.append(word)
request = (input()).lower()
for i in answer:
    if request in i.lower():
        print(i)