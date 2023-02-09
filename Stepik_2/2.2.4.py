num = [int(c) for c in input().split()]

num = ['x'] + num
num[0] = num[-1]
num = num[:-1]
print(*num)