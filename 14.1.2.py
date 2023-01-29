from math import *

def compute_binom(n, k):
    return factorial(n) / (factorial(k) * factorial( n - k ))

print(int(compute_binom(int(input()), int(input()))))