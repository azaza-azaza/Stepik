n = input()
a = n[:-5]
b = n[-5:]

print(int(a + b[::-1]))