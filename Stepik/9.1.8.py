num = int(input())

# num_ost = 0
num_2 = ''

while num > 1:
    num_2 = num_2 + str(num % 2)
    num = num // 2
    if num < 2:
        num_2 += '1'
    # num_2 += str(num_ost)

for i in range(len(num_2)-1, -1, -1):
    print(num_2[i], end ='')
