num = input()
#
# start = num[0]
num = int(num[1:])
answer = list()

for el in range(num):
    request = input()
    if '#' in request:
        ind = request.index('#')
        answer.append(request[:ind].rstrip())
    else:
        answer.append(request)

print(*answer, sep = '\n')
