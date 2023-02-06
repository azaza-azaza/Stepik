n = input()

if len(n) % 2 ==0:
    x = len(n)//2
else:
    x = len(n)//2+1

a = n[:x]
b = n[x:]

print(b, a, sep='')