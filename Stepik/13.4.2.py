def get_factors(num):
    digits = list()
    for i in range(1, num+1):
        if num % i == 0:
            digits.append(i)
    return len(digits)

print(get_factors(int(input())))