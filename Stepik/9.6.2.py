n = int(input())
word = input()

for i in range(len(word)):
    x = ord(word[i]) - n
    if x < 97:
        x += 26
    print(chr(x), end='')