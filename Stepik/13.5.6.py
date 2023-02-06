# число a – должно быть палиндромом;
# число b – должно быть простым;
# число c – должно быть четным.

def is_palindrome(num):
    for i in range(len(str(num))//2):
        if str(num)[i] != str(num)[-i-1]:
            return False
    return True

def is_prime(num):
    flag = True
    if num == 1:
        flag = False
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break
    return flag

def is_even(num):
    if num % 2 == 0:
        return True
    return False

def is_valid_password(password):
    data = [int(i) for i in password.split(':')]
    if len(data) != 3:
        return False
    if is_palindrome(data[0]) and is_prime(data[1]) and is_even(data[2]):
        return True
    return False

print(is_valid_password(input()))
