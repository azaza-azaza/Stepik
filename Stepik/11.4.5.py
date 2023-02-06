answer = list()

for i in range(int(input())):
    word = input()
    answer.append(word)

request = list()
for i in range(int(input())):
    word = input().lower()
    request.append(word)

for i in answer:
    count = 0
    for p in request:
        if p in i.lower():
            count += 1

    if count == len(request):
        print(i)