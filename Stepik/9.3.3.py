n = input()

n_low = 0
num = '0123456789'
for i in range(len(n)):
    if n[i] not in num:
        x = n[i].lower()
        if x == n[i]:
            n_low += 1

print(n_low)
