m, h = float(input()), float(input())

imt = m / h**2

if imt < 18.5:
    print('Недостаточная масса')
elif 1.85 <= imt <= 25:
    print('Оптимальная масса')
else:
    print('Избыточная масса')