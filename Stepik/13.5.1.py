def is_prime(num):
    flag = True
    if num == 1:
        flag = False
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break
    return flag

print(is_prime(int(input())))
