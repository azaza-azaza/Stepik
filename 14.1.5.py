# магическая дата

def is_magic(date):
    dd = int(date[0:2])
    mm = int(date[3:5])
    yy = int(date[8:])

    if dd * mm == yy:
        return True
    else:
        return False

print(is_magic(input()))