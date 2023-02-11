num = [c for c in input().split()]
unique_num = list()
count = 0

for i in num:
    if i not in unique_num:
        unique_num.append(i)
        count +=1

print(count)
