# принимает в качестве аргументов координаты концов отрезка
# и возвращает координаты точки являющейся серединой данного отрезка

def get_middle_point(x1, y1, x2, y2):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return x, y
x, y = get_middle_point(int(input()), int(input()), int(input()), int(input()))

print(x, y)