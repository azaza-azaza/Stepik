num = input().split()

for i in range(len(num)):
    num[i] = int(num[i])

n_min = min(num)
n_max = max(num)

n_min_in = num.index(n_min)
n_max_in = num.index(n_max)

num[n_min_in] = n_max
num[n_max_in] = n_min

# print(n_min_in)
# print(n_max_in)

print(*num, sep =' ')

