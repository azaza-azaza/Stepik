# Камень, ножницы, бумага, ящерица, Спок
def game(one, two):
    one_index = 99
    two_index = 99
    answer = ['камень', 'ящерица', 'Спок', 'ножницы', 'бумага','камень', 'ящерица', 'Спок', 'ножницы', 'бумага']
    for i in range(len(answer)):
        if one_index == 99 or two_index == 99:
            if answer[i] == one:
                one_index = i
            if answer[i] == two:
                two_index = i
        else:
            break
    if one_index > two_index:
        two_index += 5
    if one_index == two_index:
        return 'ничья'
    elif one_index == two_index - 1 or one_index == two_index - 3:
        return 'Тимур'
    else:
        return 'Руслан'
timur, ruslan = input(), input()

print(game(timur, ruslan))



