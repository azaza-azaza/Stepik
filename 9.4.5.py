n = input()

el = ''
count = 0

for i in range(len(n)):

    if n.count(n[i]) > count:
        el = n[i]
        count = n.count(n[i])

print(el)