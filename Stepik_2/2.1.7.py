# вставляет в заданное число запятые
# в соответствии со стандартным американским соглашением о запятых в больших числах

def add_commas(num):
    num = num[::-1]
    counter = 0
    answer = ''
    for el in num:
        counter += 1
        digit = el
        if counter == 3:
            answer += digit + ','
            counter = 0
        else:
            answer += digit
    if answer[-1] == ',':
        answer = answer[:-1]
    answer = answer[::-1]
    return answer

print(add_commas(input()))



