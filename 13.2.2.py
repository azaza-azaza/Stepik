def print_digit_sum(num):
    num_sum = 0
    for i in range(len(num)):
        num_sum += int(num[i])

    print(num_sum)

print_digit_sum(input())