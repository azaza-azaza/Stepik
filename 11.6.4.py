numbers = input().split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

numbers.sort()
print(*numbers, sep = ' ')
numbers.sort(reverse = True)
print(*numbers, sep = ' ')
