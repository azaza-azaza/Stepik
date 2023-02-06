# n = input().split()
#
# for i in n:
#     i = i + i[0]
#     i = i[1:] +'ки'
#     print(i, end = ' ')

n = [i[1:] + i[0] +'ки' for i in input().split()]
print(*n, sep = ' ')