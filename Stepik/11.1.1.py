n = int(input())

n += 96
k = list()
for i in range(97, n+1):
    letter = chr(i)
    k.append(letter)

print(k)
