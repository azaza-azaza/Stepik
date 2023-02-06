num = input().split()
count = 0

for i in range(len(num)):
    for k in range(i+1, len(num)):
        if num[i] == num[k]:
            count += 1

print(count)