n = int(input())
num = []

for i in range(n):
    digit = int(input())
    num.append(digit)

num_min = num.index(max(num))
del num[num_min]
num_max = num.index(min(num))
del num[num_max]

print(*num, sep='\n')

