text = len(input())

cost = round(text * 0.60, 2)

if text > 1:
    rub = int(cost // 1)
    kop = int(round(cost % rub,2) * 100)
    print(rub, 'р.', kop, 'коп.')
else:
    print('0 р. 60 коп.')


