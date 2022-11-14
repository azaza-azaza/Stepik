num = int(input())

count_3 = 0 #

digit = num % 10
count_digit = 0 #

count_2 = 0 #

count_more_5 = 0 #

multiplication = 1 #

count_0_5 = 0 #

while num >= 1:
    digit_1 = num % 10
    if digit_1 == 3:
        count_3 += 1
    if digit_1 == digit:
        count_digit += 1
    if digit_1 % 2 ==0:
        count_2 += 1
    if digit_1 > 5:
        count_more_5 += digit_1
    if digit_1 > 7:
        multiplication *= digit_1
    if digit_1 == 0 or digit_1 == 5:
        count_0_5 += 1
    num //= 10




print(count_3)
print(count_digit)
print(count_2)
print(count_more_5)
print(multiplication)
print(count_0_5)

