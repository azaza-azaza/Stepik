# Добро пожаловать в числовую угадайку

import math as m
import random as r

print('Добро пожаловать в числовую угадайку')
upper_num = int(input('Установите максимальное число >>>'))
num = r.randint(0, upper_num)
digit = int(input('Введите ваше число >>>'))
count = 0

def is_valid(text):
    if 1 <= int(text) <= upper_num:
        return True
    return False

while True:
    if is_valid(digit) == False:
        print('А может быть все-таки введем целое число от 1 до', upper_num, '?')
        digit = int(input('Введите число >>>'))
    else:
        if digit < num:
            count += 1
            print('Ваше число меньше загаданного, попробуйте еще разок')
            digit = int(input('Введите число >>>'))
        elif digit > num:
            count += 1
            print('Ваше число больше загаданного, попробуйте еще разок')
            digit = int(input('Введите число >>>'))
        else:
            print('Вы угадали, поздравляем!')
            print('Понадобилось всего', count, 'попыток!')
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')

            break