n = int(input())

count = 0
for i in range(n):
    word = input()
    if word.count('11') > 2:
        count+= 1

print(count)

