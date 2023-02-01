import random as r

digits = '23456789'
lowercase_letters = 'abcdefghjkmnpqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKMNPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
punctuation_il1Lo0O = 'il1Lo0O'

chars = ''

hom_much = int(input('Количество паролей для генерации >>> '))
how_long = int(input('Длина пароля >>> '))
want_digits = input('Включать цифры в пароль? (да/нет) >>> ').lower()
up_letters = input('Включать прописные буквы в пароль? (да/нет) >>> ').lower()
low_letters = input('Включать строчные буквы в пароль? (да/нет) >>> ').lower()
symbols = input('Включать символы в пароль? (да/нет) >>> ').lower()
symbols_il1Lo0O = input('Исключить символы il1Lo0O из пароля?? (да/нет) >>> ').lower()

if want_digits == 'да':
    chars += digits
if up_letters == 'да':
    chars += uppercase_letters
if low_letters == 'да':
    chars += lowercase_letters
if symbols == 'да':
    chars += punctuation
if symbols_il1Lo0O == 'нет':
    chars += punctuation_il1Lo0O

def generate_password(length, chars):
    password = ''
    for i in range(length):
        password += r.choice(chars)
    print(password)

for _ in range(hom_much):
    generate_password(how_long, chars)


