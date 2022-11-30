n = int(input())

a_zero = list()
zero = list()
b_zero = list()

for i in range(n):
    digit = int(input())
    if digit > 0:
        a_zero.append(digit)
    elif digit < 0:
        b_zero.append(digit)
    else:
        zero.append(digit)

print(*b_zero, sep = '\n')
print(*zero, sep = '\n')
print(*a_zero, sep = '\n')