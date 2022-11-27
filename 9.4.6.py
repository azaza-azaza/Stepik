    n = input()

    count = n.count('f')

    if count == 1:
        print(n.find('f'))
    elif count > 1:
        print(n.find('f'), n.rfind('f'), sep = ' ')
    else:
        print('NO')