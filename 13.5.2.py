def is_prime(num):
    flag = True
    if num == 1:
        flag = False
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break
    return flag

def get_next_prime(num):
    num += 1
    while is_prime(num) == False:
        num += 1

    return num

print(get_next_prime(int(input())))