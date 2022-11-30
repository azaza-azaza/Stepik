n = int(input())
num = []

for i in range(n):
    digit = int(input())
    num.append(digit)

for el in num:
    print(el)
print()
for k in num:
    print(k**2+2*k+1)