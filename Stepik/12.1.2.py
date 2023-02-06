num = input().split()
num_sum = 0
for i in range(len(num)):
    num_sum += int(num[i])

print('+'.join(num), num_sum, sep = '=')