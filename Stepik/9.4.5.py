n = input()

symb = ''
count = 0

for el in n:
    if n.count(el) >= count:
        count = n.count(el)
        symb = el
print(symb)

