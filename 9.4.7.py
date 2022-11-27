n = input()

a = n.find('h')
b = n.rfind('h')+1

print(n[:a], n[b:], sep ='')