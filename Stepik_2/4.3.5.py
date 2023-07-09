text = [c for c in input().split()]

el = list()
answer = list()

for i in range(len(text)):
    if len(el) == 0:
        el += text[i]
    elif el[0] == text[i]:
        el += text[i]
    else:
        answer.append(el)
        el = list()
        el += text[i]
    if i == len(text)-1:
        answer.append(el)


print(answer)