# Задача Иосифа Флавия
import math as m

def i_flavi(n ,k):
    num = 0
    for i in range(1, n+1):
        num = (num+k) % i
    return num+1


print(i_flavi(int(input()), int(input())))