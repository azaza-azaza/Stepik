# возвращает название месяца на русском или английском языке

def get_month(language, number):
    rus = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь' ]
    eng = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    if language == 'ru':
        return rus[number -1]
    elif language == 'en':
        return eng[number - 1]

print(get_month(input(), int(input())))