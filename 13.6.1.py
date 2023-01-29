# принимает в качестве аргумента радиус окружности и возвращает два значения:
# длину окружности и площадь круга, ограниченного данной окружностью

import math as m

def get_circle(radius):
    c = 2 * m.pi * radius
    s = m.pi * radius**2
    return c, s
radius = float(input())
c, s = get_circle(radius)

print(c, s)