num = [int(c) for c in input().split()]
count = 0
for i in range(len(num)-1):
    if num[i] < num[i+1]:
        count += 1
print(count)